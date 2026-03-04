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
    log_file = generate_log_filename(Path("logs"))

    for file in base_path.iterdir():

        if file.is_dir():
            continue

        # 1. Construir extensão composta
        suffix_list = file.suffixes
        cleaned = []

        for s in suffix_list:
            cleaned.append(s.lstrip(".").lower())

        full_suffix = ".".join(cleaned)

        # 2. Tenta extensão composta
        category_path = find_category(CATEGORIES, full_suffix)

        # 3. Se não tiver extensão nenhuma
        if not category_path and not suffix_list:
            category_path = ["other"]

        # 4. Se não achou composta, tenta simples
        if not category_path:
            simple_ext = file.suffix.lower().lstrip(".")
            category_path = find_category(CATEGORIES, simple_ext)

        # 5. Fallback final
        if not category_path:
            category_path = ["other"]

        destination = base_path

        for part in category_path:
            destination = destination / part

        destination.mkdir(parents=True, exist_ok=True)

        write_log(log_file, file, destination)

        shutil.move(str(file), str(destination / file.name))