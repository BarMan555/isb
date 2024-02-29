import json
import os
import logging
import math

logging.basicConfig(level=logging.INFO)

SEQUENCE_PATH = os.path.join('lab_2', 'sequence.json')

def frequency_bit_test(sequence : str) -> float:
    i_seq = list(map(int, sequence))
    result_seq = [-1 if x == 0 else x for x in i_seq]
    result_sum = sum(result_seq) / math.sqrt(len(result_seq))
    p_value = math.erfc(result_sum / math.sqrt(2))
    return p_value



if __name__ == "__main__":
    with open(SEQUENCE_PATH, 'r', encoding='utf-8') as f:
        sequence = json.load(f)

    cpp_seq = sequence['cpp']
    java_seq = sequence['java']

    print(frequency_bit_test(cpp_seq))