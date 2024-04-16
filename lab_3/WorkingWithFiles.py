import os
import json
import logging 

logging.basicConfig(level=logging.INFO)

def read_data(path : str) -> str:
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = file.read()
        return data
    except Exception as ex:
        logging.error(ex)