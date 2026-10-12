import requests
import csv
import os

# ===== CONFIGURE =====
API_KEY = "sk_0f329d884248fd891097cbb5536d7e7e4e75abce1bee522f"
VOICE_ID = "hpp4J3VqNfWAUOO0d1Us"

# JBFqnCBsd6RMkjVDRZzb Voice: George

CSV_FILE = "blank_character.csv"  #CSV in the format (Text, ID)
OUTPUT_DIR = "voice_lines"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ===== FUNCTION TO GENERATE AUDIO =====
def generate_voice(text, filename):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "text": text,
        "voice_settings": {"stability":0.5, "similarity_boost":0.75}
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Saved: {filename}")
    else:
        print(f"Failed: {text} -> {response.status_code}")

# ===== READ CSV AND GENERATE FILES =====
with open(CSV_FILE, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        line_id, text = row[1], row[0]
        output_file = os.path.join(OUTPUT_DIR, f"{line_id}.ogg")
        if not os.path.exists(output_file):   # Skip if already exists
            generate_voice(text, output_file)