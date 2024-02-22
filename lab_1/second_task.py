import os

from working_with_file import json_to_dict, dict_to_json, read_file, write_file

SETTING_PATH = "lab_1\\settings2.json"
RIGHT_ALPHABET = " оиеантсрвмлдякпзыьучжгхфйюбцщэъ"

OLD_SYMBOLS = "МХ4У1rb<7cЕО>А2ДКЫФa5ЛtЬРП8ЙИБЧ\n"
NEW_SYMBOLS = " налотгчйдсеиьпрюшмвбяущзжкхфэцы"

def make_stats(text : str) -> dict:
    """
    Finds the frequency of occurrence of a letter in a word.
    Return dict(letter : frequency)

    parameters
    ----------
    text : str,
        Text for analysis
    """
    length = len(text)
    stats = dict()
    for letter in text:
        if letter not in stats:
            count = text.count(letter)
            stats[letter] = count / length
    stats = dict(sorted(stats.items(), key=lambda item:item[1], reverse=True))
    return stats


def decryption(text : str, key : dict) -> str:
    """
    Replaces old characters with new ones in the text using a dictionary. 
    Return new text

    parameters
    ----------
    text : str,
        The text in which the replacement occurs
    key : dict,
        Dictionary-key
    """
    for old, new in key.items():
        text = text.replace(old, new)
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
    decrypted_path = os.path.join(
        setting['fold_lab'],
        setting['fold_task'],
        setting['decryptedTxt']
    )

    freq = make_stats(text)
    dict_to_json(stats_path, freq)

    # letter_list = list(freq.keys())
    # key = dict(zip(letter_list, RIGHT_ALPHABET))
    # dict_to_json(key_path, key)

    keyDict = dict(zip(OLD_SYMBOLS, NEW_SYMBOLS))
    resultTxt = decryption(text, keyDict)
    
    dict_to_json(key_path, keyDict)
    write_file(decrypted_path, resultTxt)