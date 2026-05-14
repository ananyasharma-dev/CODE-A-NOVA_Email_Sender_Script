# file_handler.py
# Saves and loads the sent email log

import json
import os
from datetime import datetime

LOG_FILE = "email_log.json"

def save_log(sender, recipients, subject):
    logs = load_log()
    entry = {
        "from":    sender,
        "to":      recipients,
        "subject": subject,
        "time":    datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    }
    logs.append(entry)
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)

def load_log():
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []
