import argparse
import json

from SymmetricKey import SymmetricKey
from AsymmetricKey import AsymmetricalKey
from WorkingWithFiles import serialization_public_key, serialization_private_key


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mode', type=int, help='Выбор режима работы: '
                             '0 - Запускает режим генерации ключей'
                             '1 - Запускает режим шифрования'
                             '2 - Запускает режим дешифрования') 
    parser.add_argument('-s', '--settings',help="Файл с пользовательскими настройками")
    args = parser.parse_args()

    with open(args.settings, 'r', encoding='utf-8') as file:
        settings = json.load(file)

    symmetric = SymmetricKey()
    asymmetric = AsymmetricalKey()

    match args.mode:
        case 0:
            symmetric_key = symmetric.generation_symm_key()
            public_key, private_key = asymmetric.generation_asym_keys()
            serialization_public_key(public_key, settings['public_key'])
            serialization_private_key(private_key, settings['private_key'])
            asymmetric.encrypt_symm_key(settings['symmetric_key'],
                                        settings['public_key'],
                                        settings['encrypted_symmetric_key'])
        case 1:
            print(asymmetric.decrypt_symm_key(settings['encrypted_symmetric_key'],
                                        settings['private_key'],
                                        settings['decrypted_symmetric_key']))
            symmetric.encrypt_text(settings['initial_file'],
                                settings['encrypted_file'],
                                settings['decrypted_symmetric_key'])
        case 2:
            asymmetric.encrypt_symm_key(settings['symmetric_key'],
                                        settings['public_key'],
                                        settings['encrypted_symmetric_key'])
            symmetric.decrypt_text(settings['encrypted_file'],
                                settings['decrypted_file'],
                                settings['encrypted_symmetric_key'])