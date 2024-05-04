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


        
    

