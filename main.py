from flask import Flask
from threading import Thread
import time
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return "Alive"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run_flask)
    t.start()

def start_script():
    print("Starting m.py...")
    subprocess.Popen(["python3", "m.py"])  # Run m.py

# Idle prevention function (fake activity)
def prevent_idle():
    while True:
        print("Preventing VPS from going idle...")
        time.sleep(30)  # Wait for 5 minutes (adjust as needed)

# Start keep-alive server
keep_alive()

# Start your main script (m.py)
start_script()

# Start anti-idle function
prevent_idle()
