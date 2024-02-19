import json
import logging
import os
import re

ignore_list = ['\n', '.', ',', '!', '?', ' ']

def encryption(text : str, key : dict) -> str:
    resultText = ""
    for letter in text.upper():
        if letter in ignore_list:
            resultText += letter
            continue
        resultText += key[letter]
    return resultText

def read_file(path_original : str) -> str:
    with open(path_original, 'r', encoding='utf-8') as f:
        text = f.read()
    return text

def json_to_dict(path : str) -> dict:
    with open(path, 'r', encoding='utf-8') as f:
        key = json.load(f)
    return key

if __name__ == "__main__":
    with open('lab_1\settings.json', 'r', encoding='utf-8') as f:
        setting = json.load(f)

    print(encryption(read_file('lab_1\\first_task\\original.txt'), json_to_dict('lab_1\\first_task\\key.json')))
    
    
    
    