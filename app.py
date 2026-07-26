from flask import Flask, request, Response, send_from_directory
from utils.parser import parse_upload
from utils.formatter import build_user_message
import requests
import json

app = Flask(__name__, static_folder="static")

with open("prompts/diagnosis_prompt.txt", "r") as f:
    SYSTEM_PROMPT = f.read()

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3"


@app.route("/")
def index():
    return send_from_directory("static", "index.html")


@app.route("/diagnose", methods=["POST"])
def diagnose():
    file = request.files.get("file")
    machine_name = request.form.get("machine_name", "")
    extra_context = request.form.get("extra_context", "")

    if not file:
        return {"error": "No file uploaded"}, 400

    parsed_data = parse_upload(file)

    if parsed_data is None:
        return {"error": "Unsupported file type. Upload CSV, JSON, TXT, or LOG."}, 400

    user_message = build_user_message(parsed_data, machine_name, extra_context)
    full_prompt = SYSTEM_PROMPT + "\n\n" + user_message

    def stream():
        try:
            response = requests.post(
                OLLAMA_URL,
                json={
                    "model": OLLAMA_MODEL,
                    "prompt": full_prompt,
                    "stream": True
                },
                stream=True
            )

            for line in response.iter_lines():
                if line:
                    chunk = json.loads(line)
                    text = chunk.get("response", "")
                    if text:
                        yield f"data: {text}\n\n"

        except requests.exceptions.ConnectionError:
            yield "data: Error: Ollama is not running. Start it with 'ollama serve'.\n\n"

        yield "data: [DONE]\n\n"

    return Response(stream(), mimetype="text/event-stream")


if __name__ == "__main__":
    app.run(debug=True)
