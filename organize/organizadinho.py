#!/usr/bin/env python3t Path

from pathlib import Path
import argparse
from organize.core import organize, CATEGORIES

def main():
    parser = argparse.ArgumentParser(description="Organiza arquivos por categoria.")
    parser.add_argument("path", help="Diretório a ser organizado")

    args = parser.parse_args()

    base_path = Path(args.path)

    if not base_path.exists():
        print("Caminho não existe.")
        return
    
    if not base_path.is_dir():
        print("Caminho deve ser um diretório.")
        return
    
    organize(base_path, CATEGORIES)

if __name__ == "__main__":
    main()