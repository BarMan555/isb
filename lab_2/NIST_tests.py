import json
import os
import logging

from math import fabs, sqrt, erfc
from mpmath import gammainc

logging.basicConfig(level=logging.INFO)

SEQUENCE_PATH = os.path.join('lab_2', 'sequence.json')
PI_I = {1:0.2148, 2:0.3672, 3:0.2305, 4:0.1875}

def frequency_bit_test(sequence : str) -> float:
    i_seq = list(map(int, sequence))
    result_seq = [-1 if x == 0 else x for x in i_seq]
    result_sum = fabs(sum(result_seq)) / sqrt(len(result_seq))
    p_value = erfc(result_sum / sqrt(2))
    return p_value


def identical_consecutive_bits(sequence : str) -> float:
    i_seq = list(map(int, sequence))

    share_of_units = sum(i_seq) / len(i_seq) 
    if fabs(share_of_units-(1/2)) >= 2/sqrt(len(i_seq)):
        return 0.0
    
    number_of_sign_changes = 0
    for i in range(0, len(i_seq)-1):
        number_of_sign_changes += 0 if i_seq[i] == i_seq[i+1] else 1

    p_value = erfc(
        fabs(number_of_sign_changes-2*len(i_seq)*share_of_units*(1-share_of_units))
        /(2*sqrt(2*len(i_seq))*share_of_units*(1-share_of_units))
        )
    
    return p_value


def longest_sequence_of_ones_in_the_block(sequence : str) -> float:
    i_seq = list(map(int, sequence))
    block_size = 8
    blocks = [i_seq[i:i + block_size] for i in range(0, len(i_seq), block_size)]
    v_i = {1:0, 2:0, 3:0, 4:0}
    for block in blocks:
        max_once = 0
        max_once_now = 0
        for bit in block:
            max_once_now = (max_once_now + 1) if bit == 1 else 0
            if max_once < max_once_now:
                max_once = max_once_now
        match max_once:
            case range(0, 2):
                v_i[1] += 1
            case 2:
                v_i[2] += 1
            case 3:
                v_i[3] += 1
            case range(4, 9):
                v_i[4] += 1
            case _:
                pass
    x_square = 0
    for i, v in v_i.items():
        x_square += (v-16*PI_I[i])**2 / 16*PI_I[i]
    
    p_value = gammainc(3/2, x_square/2)
    return p_value


    

if __name__ == "__main__":
    with open(SEQUENCE_PATH, 'r', encoding='utf-8') as f:
        sequence = json.load(f)

    cpp_seq = sequence['cpp']
    java_seq = sequence['java']

    print(frequency_bit_test(cpp_seq))
    print(identical_consecutive_bits(cpp_seq))
    print(longest_sequence_of_ones_in_the_block(java_seq))