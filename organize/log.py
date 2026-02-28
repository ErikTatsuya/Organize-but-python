from pathlib import Path
import datetime
import json

def generate_log_filename(base_path):
    base_path = Path(base_path)
    base_path.mkdir(exist_ok=True)
    all_files = []
    for file in base_path.iterdir():
        if file.is_file():
            all_files.append(file)

    count = len(all_files) + 1

    log_file = Path(f"log_{count}.json")
    return (base_path / log_file)

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

def log(log_file, source, destination):
    log_file.parent.mkdir(exist_ok=True)

    write_log(log_file, source, destination)

