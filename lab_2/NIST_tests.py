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


def identical_consecutive_bits(sequence : str) -> float:
    i_seq = list(map(int, sequence))

    share_of_units = sum(i_seq) / len(i_seq) 
    if math.fabs(share_of_units-(1/2)) >= 2/math.sqrt(len(i_seq)):
        return 0.0
    
    number_of_sign_changes = 0
    for i in range(0, len(i_seq)-1):
        number_of_sign_changes += 0 if i_seq[i] == i_seq[i+1] else 1

    p_value = math.erfc(
        math.fabs(number_of_sign_changes-2*len(i_seq)*share_of_units*(1-share_of_units))
        /(2*math.sqrt(2*len(i_seq))*share_of_units*(1-share_of_units))
        )
    
    return p_value




if __name__ == "__main__":
    with open(SEQUENCE_PATH, 'r', encoding='utf-8') as f:
        sequence = json.load(f)

    cpp_seq = sequence['cpp']
    java_seq = sequence['java']

    print(frequency_bit_test(cpp_seq))
    print(identical_consecutive_bits(cpp_seq))