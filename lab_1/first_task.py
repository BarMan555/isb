import json
import logging
import os
import re


def read_file(path_original : str) -> str:
    with open(path_original, 'r', encoding='utf-8') as f:
        text = f.read()
    return text

if __name__ == "__main__":
    with open('lab_1\settings.json') as f:
        setting = json.load(f)
    
    
    