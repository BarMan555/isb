import logging
import multiprocessing as mp
import hashlib


def check_number_card(tested_part : int, hash: str, last_digits : str, bins : list) -> str | None:
    """
    """
    for bin in bins:
        card_number = f'{bin}{tested_part}{last_digits}'
        if hashlib.sha224(card_number.encode()).hexdigest() == hash:
            return card_number
    return None

