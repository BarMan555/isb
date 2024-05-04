import logging
import multiprocessing as mp
import hashlib
import json
import time
from matplotlib import pyplot as plt

logging.basicConfig(level=logging.INFO)


def check_number_card(tested_part : int, hash: str, last_digits : str, bins : list) -> str | None:
    """
    """
    for bin in bins:
        card_number = f'{bin}{tested_part:06d}{last_digits}'
        if hashlib.sha224(card_number.encode()).hexdigest() == hash:
            return card_number
    return None


def number_search(save_path : str, hash : str, last_digits : str, bins : list) -> str:
    """
    """
    card_numbers = list()
    with mp.Pool(mp.cpu_count()) as p:
        for result in p.starmap(check_number_card, [(i, hash, last_digits, bins) for i in range(0, 999999)]):
            if result is not None:
                card_numbers.append(result)
    try:      
        with open(save_path, mode='w',  encoding="utf-8") as file:
            json.dump({"card_numbers": card_numbers}, file)
    except Exception as ex:
        logging.error(f"Error - {ex}")


def luna_algorithm(card_number : str) -> bool:
    """
    """
    try:
        check_digit = int(card_number[-1])
        card_number_list = [int(card_number[-i]) for i in range(2, len(card_number))]
        for i in range(len(card_number_list)):
            if(i%2==0):
                card_number_list[i] *= 2
                if card_number_list[i] >= 10:
                    card_number_list[i] = (card_number_list[i] % 10) + (card_number_list[i] // 10)

        sum_ditits = sum(card_number_list)
        check_sum = (10 - ((sum_ditits % 10)%10))
        return check_sum == check_digit
    except Exception as ex:
        logging.error(ex)


def analysis_time_search_hash_collision(hash : str, last_digits : str, bins : list):
    """
    """
    times = list()
    for i in range(1, int(mp.cpu_count()*1.5)):
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
    

