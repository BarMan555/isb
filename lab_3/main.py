import argparse
import json

from SymmetricKey import SymmetricKey
from AsymmetricKey import AsymmetricalKey
from WorkingWithFiles import serialization_public_key, serialization_private_key


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required = True)
    group.add_argument('-gen','--generation', action='store_true', help='Запускает режим генерации ключей')
    group.add_argument('-enc','--encryption', action='store_true', help='Запускает режим шифрования')
    group.add_argument('-dec','--decryption', action='store_true', help='Запускает режим дешифрования')
    parser.add_argument('-s', '--settings',help="Файл с пользовательскими настройками")
    args = parser.parse_args()

    with open(args.settings, 'r', encoding='utf-8') as file:
        settings = json.load(file)

    symmetric = SymmetricKey()
    asymmetric = AsymmetricalKey()

    if args.generation:
        symmetric_key = symmetric.generation_symm_key()
        public_key, private_key = asymmetric.generation_asym_keys()
        serialization_public_key(public_key, settings['public_key'])
        serialization_private_key(private_key, settings['private_key'])
        asymmetric.encrypt_symm_key(settings['symmetric_key'],
                                    settings['public_key'],
                                    settings['encrypted_symmetric_key'])
    elif args.encryption:
        print(asymmetric.decrypt_symm_key(settings['encrypted_symmetric_key'],
                                    settings['private_key'],
                                    settings['decrypted_symmetric_key']))
        symmetric.encrypt_text(settings['initial_file'],
                               settings['encrypted_file'],
                               settings['decrypted_symmetric_key'])
    else:
        asymmetric.encrypt_symm_key(settings['symmetric_key'],
                                    settings['public_key'],
                                    settings['encrypted_symmetric_key'])
        symmetric.decrypt_text(settings['encrypted_file'],
                               settings['decrypted_file'],
                               settings['encrypted_symmetric_key'])