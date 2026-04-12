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

    # pega os últimos logs (mais recentes primeiro)
    selected_logs = log_file_paths[::-1][:undo_amount]

    for log_file in selected_logs:
        print(f"Undoing {log_file.name}")

        with open(log_file, "r") as file:
            actions = [json.loads(line) for line in file]

        # desfaz ações na ordem inversa
        for action in reversed(actions):
            source = Path(action["destination"])   # onde o arquivo está agora
            destination = Path(action["source"])   # onde ele deveria voltar

            print(f"Source: {source}")
            print(f"Destination: {destination}")

            if source.exists():
                # garante que a pasta de destino existe
                destination.parent.mkdir(parents=True, exist_ok=True)

                shutil.move(str(source), str(destination))
                print(f"Moved back: {source} -> {destination}")
            else:
                print(f"Skipped (missing source): {source}")