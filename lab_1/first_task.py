import logging
import os
from working_with_file import write_file, read_file, json_to_dict

logging.basicConfig(level=logging.INFO)

SETTING_PATH = 'lab_1\settings1.json'
RUSSIAN = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
DIGITAL = "0123456789"

def encryption(text : str, key : dict) -> str:
    """
    Encrypts the received text using the received key. Returns the ciphertext

    parameters
    ----------
    text : str,
        Original text
    key : dict,
        Encryption key
    """
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
    
    
    
    