from flask import Flask
from threading import Thread
import time
import subprocess
from pynput.keyboard import Controller

app = Flask(__name__)

@app.route('/')
def index():
    return "Alive"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run_flask)
    t.start()

def start_bot():
    print("Starting bot...")
    subprocess.Popen(["python3", "bot.py"])  # Bot ko run karega

def auto_spacebar():
    keyboard = Controller()
    while True:
        keyboard.press(" ")
        keyboard.release(" ")
        print("Spacebar pressed!")
        time.sleep(10)  # Har 10 sec me spacebar press karega

# Flask Server Start Karo
keep_alive()

# Bot Start Karo
start_bot()

# Auto Spacebar Start Karo
auto_spacebar()
