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
    
    resultTxt = letter_dechiper(text, 'М', ' ')
    resultTxt = letter_dechiper(resultTxt, 'Х', 'н')
    resultTxt = letter_dechiper(resultTxt, '4', 'а')
    resultTxt = letter_dechiper(resultTxt, 'У', 'л')
    resultTxt = letter_dechiper(resultTxt, '1', 'о')
    resultTxt = letter_dechiper(resultTxt, 'r', 'т')
    resultTxt = letter_dechiper(resultTxt, 'b', 'г')
    resultTxt = letter_dechiper(resultTxt, '<', 'ч')
    resultTxt = letter_dechiper(resultTxt, '7', 'й')
    resultTxt = letter_dechiper(resultTxt, 'c', 'д')
    resultTxt = letter_dechiper(resultTxt, 'Е', 'с')
    resultTxt = letter_dechiper(resultTxt, 'О', 'е')
    resultTxt = letter_dechiper(resultTxt, '>', 'и')
    resultTxt = letter_dechiper(resultTxt, 'А', 'ь')
    resultTxt = letter_dechiper(resultTxt, '2', 'п')
    resultTxt = letter_dechiper(resultTxt, 'Д', 'р')
    resultTxt = letter_dechiper(resultTxt, 'К', 'ю')
    resultTxt = letter_dechiper(resultTxt, 'Ы', 'ш')
    resultTxt = letter_dechiper(resultTxt, 'Ф', 'м')
    resultTxt = letter_dechiper(resultTxt, 'a', 'в')
    resultTxt = letter_dechiper(resultTxt, '5', 'б')
    resultTxt = letter_dechiper(resultTxt, 'Л', 'я')
    resultTxt = letter_dechiper(resultTxt, 't', 'у')
    resultTxt = letter_dechiper(resultTxt, 'Ь', 'щ')
    resultTxt = letter_dechiper(resultTxt, 'Р', 'з')
    resultTxt = letter_dechiper(resultTxt, 'П', 'ж')
    resultTxt = letter_dechiper(resultTxt, '8', 'к')
    resultTxt = letter_dechiper(resultTxt, 'Й', 'х')
    resultTxt = letter_dechiper(resultTxt, 'И', 'ф')
    resultTxt = letter_dechiper(resultTxt, 'Б', 'э')
    resultTxt = letter_dechiper(resultTxt, 'Ч', 'ц')
    resultTxt = letter_dechiper(resultTxt, '\n', 'ы')



    write_file("lab_1\\second_task\\de.txt", resultTxt)