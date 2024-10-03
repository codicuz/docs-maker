import sys
import argparse

def cli():
    parser = argparse.ArgumentParser(prog='docs-maker', description='Конструктор документов')
    parser.add_argument('--version', '-v', action='version', version=f'%(prog)s Версия 0.1.0')

    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
