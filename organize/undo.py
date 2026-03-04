from pathlib import Path
import json
import shutil


def undo(undo_amount: int):
    logs_dir = Path("logs")

    if not logs_dir.exists():
        print("No logs directory found.")
        return

    log_file_paths = sorted(
        logs_dir.glob("log_*.json"),
        key=lambda p: int(p.stem.split("_")[1])
    )

    if not log_file_paths:
        print("No logs found.")
        return
    print(log_file_paths)

    reversed_logs = reversed(log_file_paths)
    selected_logs = reversed_logs[:undo_amount]

    for log_file in reversed(selected_logs):
        print(f"Undoing {log_file.name}")

        with open(log_file, "r") as file:
            actions = [json.loads(line) for line in file]

        for action in reversed(actions):
            source = Path(action["destination"])
            destination = Path(action["source"])
            print(f"Source: {source}")
            print(f"Destination: {destination}")

            if destination.exists() and destination.is_file():
                shutil.move(str(source), str(destination))
                #print(f"Moved back: {destination} -> {source}")
            else:
                ()
                #print(f"Skipped (missing): {destination}")