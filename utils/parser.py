import pandas as pd
import json

def parse_upload(file):
    filename = file.filename.lower()

    if filename.endswith(".csv"):
        df = pd.read_csv(file)
        return df.to_string(index=False)

    elif filename.endswith(".json"):
        content = file.read().decode("utf-8")
        data = json.loads(content)
        return json.dumps(data, indent=2)

    elif filename.endswith(".txt") or filename.endswith(".log"):
        content = file.read().decode("utf-8")
        return content

    else:
        return None