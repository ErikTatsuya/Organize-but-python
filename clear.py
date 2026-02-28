from pathlib import Path
import shutil

def main():
    logs = Path('logs')
    if logs.exists() and logs.is_dir():
        shutil.rmtree(logs)
    logs.mkdir()

if __name__ == '__main__':
    main()