#!/usr/bin/python3

"""
This program generates a Hamming(7, 4) or a Hamming(15, 11) code. The codes can
be extended to (8, 4) and (16, 11) for an added parity check over the entire
value. An explanation of the Hamming(7, 4) code is found on the following site:
https://en.wikipedia.org/wiki/Hamming(7,4)#
"""

from Matrix import Matrix as mat
import inquirer


# Hamming(7, 4) Generator Matrix
# | p1 p2 d3 p4 d5 d6 d7 |
# | d3 d5 d6 d7 |
hamming_7_4_G = [
    [1, 1, 0, 1], # d3, d5, d7 - starting with p1 (check 1, skip 1), XOR bits at 1, 0, 1, 0, 1, 0, 1
    [1, 0, 1, 1], # d3, d6, d7 - starting with p2 (check 2, skip 2), XOR bits at 0, 1, 1, 0, 0, 1, 1
    [1, 0, 0, 0],
    [0, 1, 1, 1], # d5, d6, d7 - statring with p4 (check 4, skip 4), XOR bits at 0, 0, 0, 1, 1, 1, 1
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
]

# Hamming(7, 4) Parity Check Matrix
hamming_7_4_H = [
    [1, 0, 1, 0, 1, 0, 1],
    [0, 1, 1, 0, 0, 1, 1],
    [0, 0, 0, 1, 1, 1, 1]
]

# Hamming(15, 11) Generator Matrix
# | p1 p2 d3 p4 d5 d6 d7 p8 d9 d10 d11 d12 d13 d14 d15 |
# | d3 d5 d6 d7 d9 d10 d11 d12 d13 d14 d15 |
hamming_15_11_G = [
    [1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1], # d3, d5, d7, d9, d11, d13, d15    - starting with p1 (check 1, skip 1), XOR bits at 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1
    [1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], # d3, d6, d7, d10, , d11, d14, d15 - starting with p2 (check 2, skip 2), XOR bits at 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1], # d5, d6, d7, d12, d13, d14, d15S  - starting with p4 (check 4, skip 4), XOR bits at 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1], # d9, d10, d11, d12, d13, d14, d15 - starting with p5 (check 8, skip 8), XOR bits at 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1
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
        value = input('Enter a hexadecimal number betwween 0x0 and 0xf inclusive to encode:\n')
        while int(value, 16) > 15 or int(value, 16) < 0:
            value = input('Please enter a value between 0x0 and 0xf inclusive:\n')
    else:
        hamming_matrix = hamming_15_11_G
        parity_check_matrix = hamming_15_11_H
        value = input('Enter a hexadecimal number betwween 0x0 and 0x7ff inclusive to encode:\n')
        while int(value, 16) > 2047 or int(value, 16) < 0:
            value = input('Please enter a value between 0x0 and 0x7ff inclusive:\n')
    value = int(value, 16)

    value_to_encode = mat(4, 1)

    for x in range(bit_depth):
        if value & 2**x:
            value_to_encode.data.append([1])
        else:
            value_to_encode.data.append([0])

    value_to_encode.print()
    encoding = mat.multiply(hamming_matrix, value_to_encode)
    parity_mod_2(encoding)

    if extra_parity:
        parity = 0
        for element in encoding:
            parity += element[0]
        encoding.append([parity % 2])

    mat.print(mat.transpose(encoding))

    parity_check = mat.multiply(parity_check_matrix, encoding)
    parity_mod_2(parity_check)
    print('Parity check:')
    mat.print_matrix(mat.transpose
    (parity_check))

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
