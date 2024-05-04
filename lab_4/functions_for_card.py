import logging
import multiprocessing as mp
import hashlib
import json

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
    check_digit = int(card_number[-1])
    card_number_list = [int(card_number[-i]) for i in range(1, len(card_number))]
    for i in card_number_list:
        card_number_list[i] *= 2
        if card_number_list[i] >= 10:
            card_number_list[i] = (card_number[i] % 10) + (card_number[i] // 10)

    sum = sum(card_number_list)
    check_sum = (10 - (sum % 10)) % 10
    return check_sum == check_digit


        
    

