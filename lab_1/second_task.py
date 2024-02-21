import os
from working_with_file import json_to_dict, dict_to_json, read_file, write_file

SETTING_PATH = "lab_1\\settings2.json"
RIGHT_ALPHABET = " оиеантсрвмлдякпзыьучжгхфйюбцщэъ"

def make_stats(text : str) -> dict:
    length = len(text)
    stats = dict()
    for letter in text:
        if letter not in stats:
            count = text.count(letter)
            stats[letter] = count / length
    stats = dict(sorted(stats.items(), key=lambda item:item[1], reverse=True))
    return stats


def dechiper(text : str, key : dict) -> str:
    for old, new in key.items():
        letter_dechiper(text, old, new)
    return text

def letter_dechiper(text : str, old : str, new : str) -> str:
    text=text.replace(old, new)
    return text

if __name__ == "__main__":
    setting = json_to_dict(SETTING_PATH)
    text = read_file(os.path.join(
        setting['fold_lab'],
        setting['fold_task'],
        setting['cipherTxt']
    ))
    stats_path = os.path.join(
        setting['fold_lab'],
        setting['fold_task'],
        setting['statsJson']
    )
    key_path = os.path.join(
        setting['fold_lab'],
        setting['fold_task'],
        setting['keyJson']
    )

    freq = make_stats(text)
    dict_to_json(stats_path, freq)

    # letter_list = list(freq.keys())
    # key = dict(zip(letter_list, RIGHT_ALPHABET))
    # dict_to_json(key_path, key)
    
    resultTxt = dechiper(text, json_to_dict(key_path))
    resultTxt = resultTxt.replace('ъ', ' ')
    write_file("lab_1\\second_task\\de.txt", resultTxt)