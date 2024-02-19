import os
from working_with_file import json_to_dict, dict_to_json, read_file

SETTING_PATH = "lab_1\\settings2.json"

def make_stats(text : str) -> dict:
    length = len(text)
    stats = dict()
    for letter in text:
        if letter not in stats:
            count = text.count(letter)
            stats[letter] = count / length
    stats = dict(sorted(stats.items(), key=lambda item:item[1], reverse=True))
    return stats


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
    dict_to_json(stats_path, make_stats(text))