import os
from datetime import datetime

def save_session_data(data_type, content):
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    folder = "sessions"
    os.makedirs(folder, exist_ok=True)

    filename = f"{folder}/{data_type}_{timestamp}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

    return filename
