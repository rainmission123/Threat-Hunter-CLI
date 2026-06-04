import datetime
import os


LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "threat_hunter.log")


def log_event(message, level="INFO"):
    os.makedirs(LOG_DIR, exist_ok=True)
    timestamp = datetime.datetime.now().isoformat(timespec="seconds")

    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(f"[{timestamp}] [{level}] {message}\n")


def log_error(message):
    log_event(message, "ERROR")
