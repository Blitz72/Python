#!/usr/bin/python3

"""
This program generates a Hamming(7, 4) or a Hamming(15, 11) code. The codes can
be extended to (8, 4) and (16, 11) for an added parity check over the entire
value. An explanation of the Hamming(7, 4) code is found on the following site:
https://en.wikipedia.org/wiki/Hamming(7,4)#
"""

import matrix as mat
import inquirer


# Hamming(7, 4) Generator Matrix
hamming_7_4_G = [
    [1, 1, 0, 1],
    [1, 0, 1, 1],
    [1, 0, 0, 0],
    [0, 1, 1, 1],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]

# Hamming(7, 4) Parity Check Matrix
hamming_7_4_H = [
    [1, 0, 1, 0, 1, 0, 1],
    [0, 1, 1, 0, 0, 1, 1],
    [0, 0, 0, 1, 1, 1, 1]
]

# Hamming(15, 11) Generator Matrix
hamming_15_11_G = [
    [1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
]

# Hamming(15, 11) Parity Check Matrix
hamming_15_11_H = [
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
    [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
]

def parity_mod_2(_matrix):
    for element in _matrix:
        if isinstance(element, list):
            if len(element) > 1:
                for x in range(len(element)):
                    element[x] %= 2
            else:
                element[0] %= 2
        else:
            element %= 2

def Hamming_code(_options):
    bit_depth = _options['bit_depth']
    extra_parity = _options['extra_parity']

    if bit_depth == 4:
        hamming_matrix = hamming_7_4_G
        parity_check_matrix = hamming_7_4_H
        value = input('Enter a hexadecimal number betwween 0x0 and 0xf to encode:\n')
        while int(value, 16) > 15 or int(value, 16) < 0:
            value = input('Please enter a value between 0x0 and 0xf:\n')
    else:
        hamming_matrix = hamming_15_11_G
        parity_check_matrix = hamming_15_11_H
        value = input('Enter a hexadecimal number betwween 0x0 and 0x7ff to encode:\n')
        while int(value, 16) > 2047 or int(value, 16) < 0:
            value = input('Please enter a value between 0x0 and 0x7ff:\n')
    value = int(value, 16)

    value_to_encode = []

    for x in range(bit_depth):
        if value & 2**x:
            value_to_encode.append([1])
        else:
            value_to_encode.append([0])

    encoding = mat.matrix_mult(hamming_matrix, value_to_encode)
    parity_mod_2(encoding)

    if extra_parity:
        parity = 0
        for element in encoding:
            parity += element[0]
        encoding.append([parity % 2])

    mat.print_matrix(mat.transpose_matrix(encoding))
    '.;-.πæ[]'
    parity_check = mat.matrix_mult(parity_check_matrix, encoding)
    parity_mod_2(parity_check)
    print('Parity check:')
    mat.print_matrix(mat.transpose_matrix(parity_check))

    encoding_int = 0
    for i in range(len(encoding)):
        encoding_int += 2**i * encoding[i][0]
    
    return hex(encoding_int)

def prompt():
    choice_list = [
        'Hamming(7, 4)',
        'Hamming(8, 4)',
        'Hamming(15, 11)',
        'Hamming(16, 11)'
    ]

    query = [
        inquirer.List(
            'hamming_type',
            message='What type of Hamming code would you like to use to encode a value?',
            choices=choice_list
        )
    ]

    answer = inquirer.prompt(query)

    options = {}
    if answer['hamming_type'] == choice_list[0]:
        options = {
            'extra_parity': False,
            'bit_depth': 4
        }
    elif answer['hamming_type'] == choice_list[1]:
        options = {
            'extra_parity': True,
            'bit_depth': 4
        }
    elif answer['hamming_type'] == choice_list[2]:
        options = {
            'extra_parity': False,
            'bit_depth': 11
        }
    elif answer['hamming_type'] == choice_list[3]:
        options = {
            'extra_parity': True,
            'bit_depth': 11
        }

    encoded_value = Hamming_code(options)
    print('Hamming encoded vale:')
    print(encoded_value, '\n')

    choice = inquirer.confirm(
        'Encode another value?',
        default=False
    )

    if choice:
        prompt()


if __name__ == '__main__':
    prompt()
