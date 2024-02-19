import json
import logging
import os
import re

RUSSIAN = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
DIGITAL = "0123456789"

def encryption(text : str, key : dict) -> str:
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

def read_file(path_original : str) -> str:
    with open(path_original, 'r', encoding='utf-8') as f:
        text = f.read()
    return text

def json_to_dict(path : str) -> dict:
    with open(path, 'r', encoding='utf-8') as f:
        key = json.load(f)
    return key

def write_file(path : str, text : str) -> None:
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

if __name__ == "__main__":
    setting = json_to_dict('lab_1\settings.json')
    text = encryption(read_file('lab_1\\first_task\\original.txt'), 
                      json_to_dict('lab_1\\first_task\\key.json'))
    write_file('lab_1\\first_task\\result.txt', text)
    
    
    
    