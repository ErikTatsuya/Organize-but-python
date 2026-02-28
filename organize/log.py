from pathlib import Path
import datetime
import json

def generate_log_filename(base_path):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    return base_path / f"organize_log_{timestamp}.json"

def write_log(log_file, source, destination):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = {
        "timestamp": timestamp,
        "action": "move",
        "source": str(source),
        "destination": str(destination)
    }

    with open(log_file, "a") as file:
        json.dump(log_entry, file)
        file.write("\n")

def log(source, destination):
    log_file = generate_log_filename(Path("logs"))
    log_file.parent.mkdir(exist_ok=True)

    write_log(log_file, source, destination)

