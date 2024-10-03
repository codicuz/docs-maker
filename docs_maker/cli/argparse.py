import sys
import argparse
import docs_maker

def cli():
    parser = argparse.ArgumentParser(prog='docs-maker', description='Конструктор документов')
    parser.add_argument('-v', '--version', action='version', version=f'%(prog)s Версия 0.1.0')
    parser.add_argument('-r', '--run', action='store_true', help='Запустить')

    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()

    if args.run:
        db = docs_maker.InitDb()
        db.init()
