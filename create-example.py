from pathlib import Path
import shutil

def create_example(dir_path):
    dir_path = Path(dir_path)

    shutil.rmtree(dir_path, ignore_errors=True)

    dir_path.mkdir(exist_ok=True)

    (dir_path / "video.mp4").touch()
    (dir_path / "movie.mkv").touch()
    (dir_path / "clip.mov").touch()

    (dir_path / "photo.jpg").touch()
    (dir_path / "image.png").touch()
    (dir_path / "animation.gif").touch()

    (dir_path / "song.mp3").touch()
    (dir_path / "recording.wav").touch()
    (dir_path / "audio.opus").touch()

    (dir_path / "document.txt").touch()
    (dir_path / "presentation.pptx").touch()
    (dir_path / "report.pdf").touch()

    (dir_path / "archive.zip").touch()
    (dir_path / "backup.tar.gz").touch()
    (dir_path / "package.deb").touch()

if __name__ == "__main__":
    dir_path = "example"
    create_example(dir_path)