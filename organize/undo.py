from pathlib import Path
from organize.log import get_logs_sorted
import shutil

def undo_organize():
    logs = get_logs_sorted()

    if not logs:
        return "no logs found"

    latest_log = logs[0]