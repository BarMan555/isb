import json
import logging
import os
import re

logging.basicConfig(level=logging.INFO)

SETTING_PATH = 'lab_1\settings.json'
RUSSIAN = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
DIGITAL = "0123456789"

def encryption(text : str, key : dict) -> str:
    try:
        # Создаем таблицу регистров для коректного выходного
        registerTable = list()
        for letter in text:
            if (letter not in RUSSIAN) and (letter not in DIGITAL): continue
            if letter.isupper():
                registerTable.append(True)
            else:
                registerTable.append(False)
            
        # Создаем новую строчку с закодированным текстом
        # учитывая регистор с помощью таблицы регистров
        i = 0
        resultText = ""
        for letter in text.upper():
            if (letter not in RUSSIAN) and (letter not in DIGITAL):
                resultText += letter
                continue

            resultKey = key[letter]
            if registerTable[i]: resultText += resultKey
            else:                resultText += resultKey.lower()
            i += 1
        
        return resultText
    except Exception as ex:
        logging.error(ex)

def read_file(path_original : str) -> str:
    try:
        with open(path_original, 'r', encoding='utf-8') as f:
            text = f.read()
        return text
    except FileNotFoundError as ex:
        logging.error(ex)

def json_to_dict(path : str) -> dict:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            key = json.load(f)
        return key
    except Exception as ex:
        logging.error(ex)

def write_file(path : str, text : str) -> None:
    try:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text)
    except Exception as ex:
        logging.error(ex)

if __name__ == "__main__":
    setting = json_to_dict(SETTING_PATH)
    original_path = os.path.join(setting["fold_lab"], 
                                 setting["fold_task"], 
                                 setting["originalTxt"])
    key_path = os.path.join(setting["fold_lab"], 
                            setting["fold_task"], 
                            setting["keyJson"])
    result_path = os.path.join(setting["fold_lab"], 
                            setting["fold_task"], 
                            setting["resultTxt"])
    
    text = encryption(read_file(original_path), 
                      json_to_dict(key_path))
    write_file(result_path, text)
    
    
    
    