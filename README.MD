# Malicious Keylogger Script - WARNING

## ⚠️ CRITICAL WARNING: ILLEGAL AND DANGEROUS SOFTWARE ⚠️

This project demonstrates how malicious keyloggers operate and is intended strictly for cybersecurity education, malware analysis, and defensive security research in controlled environments.

Unauthorized deployment, distribution, or use of this software against systems you do not own or explicitly have permission to test is illegal in many countries.

---

# What This Script Does

This Python script demonstrates several techniques commonly used by malicious keyloggers and information-stealing malware.

## 1. Keystroke Logging

The script captures keyboard activity on the target system, including:

- Regular text characters
- Special keys (Shift, Ctrl, Alt, etc.)
- Space bar
- Function keys (F1-F12)
- Arrow/navigation keys
- Other keyboard input events

---

## 2. Data Transmission

The script periodically sends captured keystrokes to a remote Telegram bot using the Telegram API.

Features include:

- Configurable reporting intervals
- Automatic background reporting
- Basic error handling if internet connectivity fails

---

## 3. Persistence Mechanism

The script demonstrates persistence techniques commonly used by malware:

- Copies itself to the Windows AppData directory
- Adds itself to Windows startup registry keys
- Launches automatically on user login
- Hides the executable using Windows file attributes

---

## 4. Stealth Behavior

The script attempts to operate silently by:

- Running without a visible window
- Hiding background execution
- Using hidden file attributes
- Avoiding user interaction

---

# Prerequisites (Educational Analysis Only)

## Required Python Libraries

Install dependencies using:

```bash
pip install pynput requests python-dotenv
```

or:

```bash
pip install -r requirements.txt
```

---

## Supported Environment

- Windows 10 / Windows 11
- Python 3.x
- Internet access
- Administrative permissions may be required for registry modifications

---

# Configuration

The script uses environment variables stored inside a `.env` file.

Example configuration:

```env
# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN=YOUR_BOT_TOKEN_HERE
TELEGRAM_CHAT_ID=YOUR_CHAT_ID_HERE
REPORT_INTERVAL=60
PERSISTENCE_FILENAME=winlog.exe
```

---

# Environment Variable Loading

```python
import os
import dotenv

dotenv.load_dotenv()

bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
chat_id = os.getenv('TELEGRAM_CHAT_ID')
interval = int(os.getenv('REPORT_INTERVAL', 60))
filename = os.getenv('PERSISTENCE_FILENAME', 'winlog.exe')
```

---

# Telegram Configuration

## Create a Telegram Bot

1. Open Telegram
2. Search for `@BotFather`
3. Send `/newbot`
4. Follow the instructions
5. Save the generated bot token

---

## Obtain Your Chat ID

1. Start a chat with your bot
2. Visit:

```text
https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
```

3. Find your chat ID in the JSON response

---

# Usage Instructions

## ⚠️ WARNING

Running this script on systems without explicit authorization may violate privacy laws, cybersecurity laws, and computer crime legislation.

Use only inside:

- Virtual machines
- Malware analysis labs
- Sandboxed environments
- Systems you own

---

## Run the Script

```bash
python keylogger.py
```

---

## Build as Executable (Optional)

```bash
pip install pyinstaller
pyinstaller --noconsole --onefile keylogger.py
```

---

# Behavior Overview

When executed, the script:

1. Checks whether it already exists in the hidden directory
2. Copies itself into `%APPDATA%`
3. Marks the file as hidden
4. Creates a Windows startup registry entry
5. Launches a persistent hidden instance
6. Begins recording keyboard input
7. Sends logs to Telegram periodically

---

# Detection and Removal

## Detection Indicators

Security software may detect:

- Keyboard hooking activity
- Suspicious startup registry modifications
- Hidden executables inside AppData
- Outbound requests to Telegram API servers
- Unusual background Python processes

---

## Manual Removal Steps

### 1. Stop Running Processes

Open Task Manager:

```text
Ctrl + Shift + Esc
```

End suspicious processes related to the script.

---

### 2. Remove Startup Registry Entry

Open Registry Editor:

```text
regedit
```

Navigate to:

```text
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
```

Delete suspicious entries such as:

```text
WindowsUpdater
```

---

### 3. Delete Hidden Executable

Remove the copied executable from:

```text
%APPDATA%
```

---

### 4. Run Antivirus Scan

Perform a complete system scan using updated antivirus or endpoint protection software.

---

### 5. Restart the System

Reboot the computer to ensure persistence has been removed.

---

# Legal Consequences

Unauthorized use of monitoring software may violate laws including:

- Computer Fraud and Abuse Act (CFAA)
- Cybercrime legislation
- Privacy protection laws
- Data protection regulations
- Workplace surveillance restrictions

---

## Possible Penalties

Misuse may result in:

- Criminal prosecution
- Heavy financial fines
- Civil lawsuits
- Permanent criminal record
- Loss of employment
- Academic disciplinary action
- Imprisonment in severe cases

---

# Ethical and Legal Statement

This project is provided strictly for:

- Cybersecurity education
- Malware analysis
- Defensive security research
- Authorized penetration testing
- Security awareness training

You must obtain explicit written permission before testing this software on any system that you do not personally own.

The author does not support:

- Unauthorized surveillance
- Credential theft
- Privacy violations
- Malware deployment
- Illegal access to devices
- Distribution of malicious software

Any misuse of this project is solely the responsibility of the user.

---

# Educational Purpose

Understanding how keyloggers work helps security professionals:

- Build better malware detection systems
- Improve endpoint protection
- Train incident response teams
- Understand persistence techniques
- Strengthen cybersecurity defenses
- Educate users about digital threats

This knowledge must only be used for defensive and educational purposes.

---

# License

## MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.

IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY ARISING FROM THE SOFTWARE OR ITS USE.

---

# Disclaimer

This repository is intended solely for educational and defensive cybersecurity research.

The author assumes no responsibility for misuse, damages, legal consequences, or unauthorized activity involving this software.