#!/bin/bash
echo "[+] Installing dependencies..."
pip3 install flask requests html2canvas 2>/dev/null

echo "[+] Creating folders..."
mkdir -p logs static templates payloads

echo "[+] Placing placeholder files..."
touch logs/victims.txt
touch templates/dashboard.html
touch static/x.js
touch server.py

echo "[+] Launching XSS Babe!"
python3 server.py
