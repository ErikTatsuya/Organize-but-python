from organize.log import write_log, generate_log_filename
from pathlib import Path
import shutil

CATEGORIES = {
    "media": {
        "video": {
            "general": ["mp4", "mov", "mkv"],
            "editing": {
                "davinci_resolve": ["drt"]
            }
        },
        "image": {
            "general": ["jpg", "jpeg", "png", "gif"]
        },
        "audio": {
            "general": ["mp3", "opus", "wav"]
        }
    },
    "documents": {
        "text": ["txt", "pdf", "docx", "pptx"],
        "archives": ["zip", "7z", "rar", "iso", "tar.gz"]
    },
    "development": {
        "backend": ["py", "go", "java"],
        "frontend": ["js", "jsx", "html", "css"],
        "data": ["sql", "db", "csv", "json"],
        "low_level": ["asm", "c", "cpp"]
    },
    "software": {
        "executables": ["exe", "msi", "jar", "out", "flatpakref"],
        "packages": ["deb", "rpm", "apk", "appimage"]
    },
    "other": ["log"]
}

SPECIAL_FILES = {
    "development": ["makefile", "license", "readme"],
    "documents": ["changelog", "authors"]
}


def find_category(CATEGORIES, extension, path=None):
    if path is None:
        path = []

    for key, value in CATEGORIES.items():
        if isinstance(value, list):
            if extension in value:
                return path + [key] + extension.split(".")
        elif isinstance(value, dict):
            result = find_category(value, extension, path + [key])
            if result:
                return result

    return None

def find_special_file_category(special_map, filename):
    filename = filename.lower()

    for category, names in special_map.items():
        if filename in names:
            return [category]

    return None

def organize(base_path, CATEGORIES):
    base_path = Path(base_path)
    log_file = generate_log_filename("logs")

    for file in base_path.iterdir():

        if file.is_dir():
            continue

        suffix_list = file.suffixes
        cleaned = [s.lstrip(".").lower() for s in suffix_list]
        full_suffix = ".".join(cleaned)

        category_path = find_category(CATEGORIES, full_suffix)

        if not category_path and not suffix_list:
            category_path = ["other"]

        if not category_path:
            simple_ext = file.suffix.lower().lstrip(".")
            category_path = find_category(CATEGORIES, simple_ext)

        if not category_path:
            category_path = ["other"]

        destination = base_path

        for part in category_path:
            destination = destination / part

        destination.mkdir(parents=True, exist_ok=True)

        final_destination = destination / file.name

        write_log(log_file, file, final_destination)

        shutil.move(str(file), str(final_destination))