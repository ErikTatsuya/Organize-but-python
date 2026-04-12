from pathlib import Path
import shutil
import random

def create_example(base_path, rounds):
    base_path = Path(base_path)
    shutil.rmtree(base_path, ignore_errors=True)
    base_path.mkdir(exist_ok=True)

    extensions = [
        "mp4", "mkv", "mov",
        "jpg", "png", "gif",
        "mp3", "wav", "opus",
        "txt", "pptx", "pdf",
        "zip", "tar.gz", "deb"
    ]

    for _ in range(rounds):
        ext = random.choice(extensions)

        # Conta quantos arquivos já existem com essa extensão
        existing = list(base_path.glob(f"file_*.{ext}"))
        count = len(existing) + 1

        file_name = f"file_{count}.{ext}"
        (base_path / file_name).touch()

if __name__ == "__main__":
    base_path = "example"
    create_example(base_path, 10)