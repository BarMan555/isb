import logging
import json

logging.basicConfig(level=logging.INFO)

def read_file(path_original : str) -> str:
    """
    Read file. Return text from file

    parameters
    ----------
    path_original : str,
        Path to file
    """
    try:
        with open(path_original, 'r', encoding='utf-8') as f:
            text = f.read()
        return text
    except FileNotFoundError as ex:
        logging.error(ex)


def json_to_dict(path : str) -> dict:
    """
    Translate json file to dict. Return dict

    parameters
    ----------
    path : str,
        Path to JSON file
    """
    try:
        with open(path, 'r', encoding='utf-8') as f:
            key = json.load(f)
        return key
    except Exception as ex:
        logging.error(ex)


def write_file(path : str, text : str) -> None:
    """
    Write text to file

    parameters
    ----------
    path : str,
        Path to save text
    text : str,
        Text for saving
    """
    try:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text)
    except Exception as ex:
        logging.error(ex)