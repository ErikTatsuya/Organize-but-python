from pathlib import Path
from organize.log import get_logs_sorted
import shutil

def undo_organize():
    logs = get_logs_sorted()

    if not logs:
        return "no logs found"

    latest_log = logs[0]

    with open(latest_log, "r") as file:
        log_entries = file.readlines() 
    for entry in log_entries:
        if 