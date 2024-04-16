import os
import json
import logging 

logging.basicConfig(level=logging.INFO)


def write_data(text : str, path : str) -> None:
    try:
        with open(path, 'w', encoding='utf-8') as file:
            file.write(text)
    except Exception as ex:
        logging.error(ex)


def write_data_bytes(data : bytes, path : str) -> None:
    try: 
        with open(path, 'wb') as file:
            file.write(data)
    except Exception as ex:
        logging.error(ex)


def read_data(path : str) -> str:
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = file.read()
        return data
    except Exception as ex:
        logging.error(ex)


def serialization_symmetric_key(key : bytes, path : str) -> None:
    try:
        with open(path, 'wb') as key_file:
            key_file.write(key)
    except Exception as ex:
        logging.error(ex)



def deserialization_symmetric_key(path : str) -> bytes:
    try:
        with open(path, mode='rb') as key_file: 
            content = key_file.read()
        return content
    except Exception as ex:
        logging.error(ex)
