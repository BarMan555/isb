import json
import argparse

from functions_for_card import number_search, luna_algorithm, analysis_time_search_hash_collision


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mode', type=int, help='Выбор режима работы: '
                             '0 - Подобрать номер карты по ее хешу'
                             '1 - Проверить корректность номера карты при помощи алгоритма Луна'
                             '2 - Замерить время для поиска коллизии хеша при различном числе процессов') 
    group = parser.add_argument_group('Аргументы на выбор')
    group.add_argument('--info', required=False, help='Информация о карте и ёё хэш')
    group.add_argument('--numbers', required=False, help="Номер карты")
    args = parser.parse_args()

    if args.info:
        with open(args.info, 'r', encoding='utf-8') as file:
            settings = json.load(file)

    match args.mode:
        case 0:
             number_search("card_number.json", settings["hash"], settings["last_digits"], settings["bins"])
        case 1: 
            if luna_algorithm(args.numbers):
                print("Numbers is correct")
            else:
                print("Numbers is incorrect")
        case 2:
            analysis_time_search_hash_collision(settings["hash"], settings["last_digits"], settings["bins"])