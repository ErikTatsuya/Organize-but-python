#!/usr/bin/env python3t Path

from pathlib import Path
import argparse
from organize.core import organize, CATEGORIES
from organize.gui.gui import main_gui

def main():
    parser = argparse.ArgumentParser(
        prog="organize",
        description="Organizador de arquivos via CLI ou GUI"
    )

    subparsers = parser.add_subparsers(dest="command")

    # Subcomando CLI
    run_parser = subparsers.add_parser(
        "run",
        help="Organiza arquivos em um diretório"
    )
    run_parser.add_argument("path", help="Caminho do diretório")

    # Subcomando GUI
    subparsers.add_parser(
        "gui",
        help="Inicia a interface gráfica"
    )

    args = parser.parse_args()

    # Se nenhum subcomando for passado
    if args.command is None:
        parser.print_help()
        return

    if args.command == "run":
        organize(args.path, CATEGORIES)

    elif args.command == "gui":
        main_gui()

if __name__ == "__main__":
    main()