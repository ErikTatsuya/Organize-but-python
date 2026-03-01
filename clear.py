from pathlib import Path
import shutil

def clear(base_path):
    logs = Path(base_path)
    if logs.exists() and logs.is_dir():
        shutil.rmtree(logs)
    logs.mkdir()

if __name__ == '__main__':
    clear()