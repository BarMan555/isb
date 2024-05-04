import json
import logging
import hashlib
import multiprocessing as mp
import time

from tqdm import tqdm
from matplotlib import pyplot as plt

logging.basicConfig(level=logging.INFO)


def check_number_card(tested_part : int, hash: str, last_digits : str, bins : list) -> str | None:
    """
    Checks the card number with the specified number to match the hash.

    args:
        tested_part : generated part fot testing
        hash : input hash of number
        last_digits : last 4 digits of card's number
        bins : bins 
    return:
        number of card if it match with hash OR None if not 
    """
    for bin in bins:
        card_number = f'{bin}{tested_part:06d}{last_digits}'
        if hashlib.sha224(card_number.encode()).hexdigest() == hash:
            return card_number
    return None


def number_search(save_path : str, hash : str, last_digits : str, bins : list) -> str:
    """
    Search for credit card numbers, using hash, and save them to a file.
    The function uses multiple processes to reduce the search time.

    args:
        save_path: the path to save the card's number
        hash : input hash of number
        last_digits : last 4 digits of card's number
        bins : bins 
    return:
        number of card if it match with hash
    """
    card_numbers = 0
    with mp.Pool(mp.cpu_count()) as p:
        for result in p.starmap(check_number_card, [(i, hash, last_digits, bins) for i in range(0, 999999)]):
            if result is not None:
                card_numbers = result
                break
    try:      
        with open(save_path, mode='w',  encoding="utf-8") as file:
            json.dump({"card_numbers": card_numbers}, file)
    except Exception as ex:
        logging.error(ex)


def luna_algorithm(card_number : str) -> bool:
    """
    Checking the credit card number using the Moon algorithm

    args:
        card_number : number of card
    return:
        result of the check
    """
    try:
        card_number_list = [int(char) for char in card_number]
        for i in range(1, len(card_number_list)):
            if(i%2==0):
                card_number_list[i] *= 2
                if card_number_list[i] >= 10:
                    card_number_list[i] = (card_number_list[i] % 10) + (card_number_list[i] // 10)

        sum_ditits = sum(card_number_list)
        check_sum = 10 - ((sum_ditits % 10)%10)
        return check_sum == card_number_list[0]

    except Exception as ex:
        logging.error(ex)


def analysis_time_search_hash_collision(hash : str, last_digits : str, bins : list) -> None:
    """
    Measuring the time for searching for hash function collisions and
    plotting the time dependence on the number of processes spent

    args:
        hash : input hash of number
        last_digits : last 4 digits of card's number
        bins : bins 
    """
    try:
        times = list()
        for i in tqdm(range(1, int(mp.cpu_count()*1.5)), desc='Поиск колизии'):
            start = time.time()
            with mp.Pool(i) as p:
                for result in p.starmap(check_number_card, [(i, hash, last_digits, bins) for i in range(0, 999999)]):
                    if result is not None:
                        times.append(time.time() - start)
                        break
        plt.plot(range(len(times)), times, color="green", marker="o", markersize=7,)
        plt.xlabel("Количество процессов, Шт")
        plt.ylabel("Время, С")
        plt.title("График зависимости времени поиска коллизии от числа процессов")
        plt.show()
    except Exception as ex:
        logging.error(ex)

