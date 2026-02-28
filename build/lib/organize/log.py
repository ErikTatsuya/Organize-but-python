from pathlib import Path
import datetime

def log(log_file, log_data):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - {log_data}\n"

    with open(log_file, "a") as file:
        file.write(log_entry)

def generate_log_filename(base_path):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    return base_path / f"organize_log_{timestamp}.txt"

def log_organized_file(original_path, new_path):
    log_data = f"Moved: '{original_path}' to '{new_path}'"
    log_file = generate_log_filename(Path("logs"))

    log_file.parent.mkdir(parents=True, exist_ok=True)
    log_file.touch(exist_ok=True)

    log(log_file, log_data)