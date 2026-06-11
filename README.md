# Smart Fault Diagnosis System

An AI-powered fault diagnosis tool that accepts sensor data or machine error logs and returns a structured diagnosis — identifying faults, severity levels, corrective actions, and failure predictions.

Built with Flask and LLaMA 3 running locally via Ollama. No API key or internet connection required after setup.

---

## Demo

Upload a `.csv`, `.json`, `.txt`, or `.log` file containing machine sensor readings or error logs, provide the machine name and any additional context, and the system streams a full diagnosis report in real time.

---

## Features

- Accepts CSV, JSON, TXT, and LOG file formats
- Streams diagnosis output in real time
- Identifies faults with LOW / MEDIUM / HIGH severity ratings
- Suggests corrective actions and predicts imminent failures
- Runs fully offline using a local LLM — no API key needed
- Clean dark UI with no external dependencies

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| AI Model | LLaMA 3 via Ollama |
| Data Parsing | Pandas |
| Frontend | HTML, CSS, JavaScript (vanilla) |
| Streaming | Server-Sent Events (SSE) |

---

## Project Structure

```
smart-fault-diagnosis/
│
├── app.py
├── requirements.txt
│
├── prompts/
│   └── diagnosis_prompt.txt
│
├── utils/
│   ├── parser.py
│   └── formatter.py
│
└── static/
    └── index.html
```

---

## Getting Started

### Prerequisites

- Python 3.8+
- [Ollama](https://ollama.com) installed

### Installation

```bash
git clone https://github.com/your-username/smart-fault-diagnosis.git
cd smart-fault-diagnosis
pip install -r requirements.txt
```

### Run the model

```bash
ollama pull llama3
ollama serve
```

### Start the app

```bash
python app.py
```

Open `http://localhost:5000` in your browser.

---

## Sample Test Files

Sample files are provided in the `samples/` folder to test the app immediately:

| File | Format | Description |
|---|---|---|
| `sample_sensor_data.csv` | CSV | Escalating temperature, vibration, and current readings |
| `sample_error_log.log` | LOG | Machine error log with WARNING, ERROR, and CRITICAL entries |
| `sample_fault_data.json` | JSON | Structured sensor snapshot with maintenance history |

---

## How It Works

1. User uploads a sensor data or log file
2. Flask parses the file using Pandas or raw text extraction
3. Parsed data is formatted and injected into a structured system prompt
4. LLaMA 3 (running locally via Ollama) generates a streamed diagnosis
5. Output is streamed back to the UI using Server-Sent Events

---


## Author

**Mehul**
B.Tech CSE (AI & ML) — University of Engineering & Management, Kolkata
[LinkedIn](https://linkedin.com/in/your-link) • [GitHub](https://github.com/your-username)
