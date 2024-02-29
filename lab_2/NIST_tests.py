import json
import os
import logging
import math

logging.basicConfig(level=logging.INFO)

SEQUENCE_PATH = os.path.join('lab_2', 'sequence.json')



if __name__ == "__main__":
    with open(SEQUENCE_PATH, 'r', encoding='utf-8') as f:
        sequence = json.load(f)

    cpp_seq = sequence['cpp']
    java_seq = sequence['java']