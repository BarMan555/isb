import argparse
import json

from SymmetricKey import SymmetricKey
from AsymmetricKey import AsymmetricalKey


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required = True)
    group.add_argument('-gen','--generation',help='Запускает режим генерации ключей')
    group.add_argument('-enc','--encryption',help='Запускает режим шифрования')
    group.add_argument('-dec','--decryption',help='Запускает режим дешифрования')
    parser.add_argument('-s', '--settings',help="Файл с пользовательскими настройками")
    args = parser.parse_args()

    with open(args.settings, 'r', encoding='utf-8') as file:
        settings = json.load(file)

    if args.generation is not None:
        pass
    elif args.encryption is not None:
        pass
    else:
        pass