from pathlib import Path
import json
import shutil


def undo(undo_amount: int):
    logs_dir = Path("logs")

    if not logs_dir.exists():
        print("No logs directory found.")
        return

    log_files = sorted(
        logs_dir.glob("log_*.json"),
        key=lambda p: int(p.stem.split("_")[1])
    )

    if not log_files:
        print("No logs found.")
        return

    selected_logs = log_files[-undo_amount:] #

    for log_file in reversed(selected_logs):
        print(f"Undoing {log_file.name}")

        with open(log_file, "r") as f:
            actions = [json.loads(line) for line in f]

        for action in reversed(actions):
            source = Path(action["source"])
            destination = Path(action["destination"])

            if destination.exists():
                shutil.move(str(destination), str(source))
                print(f"Moved back: {destination} -> {source}")
            else:
                print(f"Skipped (missing): {destination}")