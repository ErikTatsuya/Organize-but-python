#!/usr/bin/env python3t

from organize.core import organize, CATEGORIES
from organize.gui.gui import main_gui
from organize.undo import undo
import argparse


def main():
    parser = argparse.ArgumentParser(
        prog="organize",
        description="Organizador de arquivos via CLI ou GUI"
    )

    subparsers = parser.add_subparsers(dest="command")

    # roda oraganizador pela CLI
    run_parser = subparsers.add_parser(
        "run",
        help="Organiza arquivos em um diretório"
    )
    run_parser.add_argument("path", help="Caminho do diretório")

    # roda organizador pela GUI
    subparsers.add_parser(
        "gui",
        help="Inicia a interface gráfica"
    )
    
    undo_parser = subparsers.add_parser(
        "undo",
        help="Desfaz a última operação de organização"
    )
    undo_parser.add_argument("amount", type=int, help="Número de operações para desfazer")

    args = parser.parse_args()

    #ajuda se nenhum argumento ou comando for passado
    if args.command is None:
        parser.print_help()
        return

    if args.command == "run":
        organize(args.path, CATEGORIES)

    elif args.command == "gui":
        main_gui()

    elif args.command == "undo":
        undo_amount = args.amount
        undo(undo_amount)

if __name__ == "__main__":
    main()