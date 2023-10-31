#!/usr/bin/python3

"""
This Python program is inspired from implementing the logic behind matrix
multiplication as found on the Wikipedia site:
https://en.wikipedia.org/wiki/Matrix_multiplication#

Then further expanded by implementing Hamming(7, 4) and Hamming(15, 11) codes
as found on the following site:
https://en.wikipedia.org/wiki/Hamming(7,4)#
"""

import random
import matrix as mat


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

hamming_4_7_G = [
    [1, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 1, 0, 1, 0],
    [1, 1, 0, 1, 0, 0, 1]
]

# Hamming(7, 4) Parity Check Matrix
hamming_7_4_H = [
    [1, 0, 1, 0, 1, 0, 1],
    [0, 1, 1, 0, 0, 1, 1],
    [0, 0, 0, 1, 1, 1, 1]
]

hamming_4_7_H = [
    [1, 0, 0],
    [0, 1, 0],
    [1, 1, 0],
    [0, 0, 1],
    [1, 0, 1],
    [0, 1, 1],
    [1, 1, 1]
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

hamming_11_15_G = [
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1]
]

# Hamming(15, 11) Parity Check Matrix
hamming_15_11_H = [
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
    [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
]

hamming_11_15_H = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 1, 1, 0],
    [1, 1, 1, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 0, 1],
    [1, 1, 0, 1],
    [0, 0, 1, 1],
    [1, 0, 1, 1],
    [0, 1, 1, 1],
    [1, 1, 1, 1]
]

data_7_4 = [
    [1],
    [0],
    [0],
    [0]
]

data_4_7 = [
    [0, 1, 1, 0]
]

data_15_11 = [
    [1],
    [0],
    [1],
    [1],
    [0],
    [0],
    [1],
    [0],
    [1],
    [1],
    [1]
]

data_11_15 = [
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


if __name__ == '__main__':
    hamming_result_7_4 = mat.matrix_mult(hamming_7_4_G, data_7_4)
    for result in hamming_result_7_4:
        result[0] %= 2

    print(f"Hamming(7, 4) result of {data_7_4[0][0]}{data_7_4[1][0]}{data_7_4[2][0]}{data_7_4[3][0]}:")
    mat.print_matrix(hamming_result_7_4)

    hamming_parity_check = mat.matrix_mult(hamming_7_4_H, hamming_result_7_4)
    for result in hamming_parity_check:
        result[0] %= 2

    print("Hamming parity check of previous result:")
    mat.print_matrix(hamming_parity_check)

    hamming_result_15_11 = mat.matrix_mult(hamming_15_11_G, data_15_11)
    for result in hamming_result_15_11:
        result[0] %= 2

    print("Hamming(15, 11) result of ", end='')
    for i in range (len(data_15_11) - 1):
        print(f"{data_15_11[i][0]}", end='')
    print(f"{data_15_11[len(data_15_11) - 1][0]}:")
    mat.print_matrix(hamming_result_15_11)

    # Flip a random bit in the data_11 sequence and print the matrix for comparison
    rand_int = random.randint(0, 14)
    if hamming_result_15_11[rand_int][0] == 0:
        hamming_result_15_11[rand_int][0] = 1
    else:
        hamming_result_15_11[rand_int][0] = 0

    print("Let's a flip a random bit... ;)")
    mat.print_matrix(hamming_result_15_11)

    hamming_parity_check = mat.matrix_mult(hamming_15_11_H, hamming_result_15_11)
    for result in hamming_parity_check:
        result[0] %= 2

    print("We'll use the parity check matrix to find out which bit was flipped!")
    print("Hamming parity check of previous result:")
    mat.print_matrix(hamming_parity_check)

    index = 0
    for i in range(len(hamming_parity_check)):
        index += pow(2, i) * hamming_parity_check[i][0]
    print(f"The bit in position {index} was flipped!!!")
    print('-----------------------------\n')

    hamming_result_4_7 = mat.matrix_mult(data_4_7, hamming_4_7_G)
    for result in hamming_result_4_7[0]:
        result %= 2
    for i in range(len(hamming_result_4_7[0])):
        hamming_result_4_7[0][i] %= 2
    mat.print_matrix(data_4_7)
    mat.print_matrix(hamming_result_4_7)

    hamming_parity_check_4_7 = mat.matrix_mult(hamming_result_4_7, hamming_4_7_H)
    for i in range(len(hamming_parity_check_4_7[0])):
        hamming_parity_check_4_7[0][i] %= 2
    mat.print_matrix(hamming_parity_check_4_7)

    hamming_result_11_15 = mat.matrix_mult(data_11_15, hamming_11_15_G)
    for result in hamming_result_11_15[0]:
        result %= 2
    for i in range(len(hamming_result_11_15[0])):
        hamming_result_11_15[0][i] %= 2
    mat.print_matrix(data_11_15)
    # print("hamming_result_11_15: ", hamming_result_11_15, end='')
    mat.print_matrix(hamming_result_11_15)

    print("Let's a flip a random bit... ;)")
    rand_int = random.randint(0, 14)
    if hamming_result_11_15[0][rand_int] == 0:
        hamming_result_11_15[0][rand_int] = 1
    else:
        hamming_result_11_15[0][rand_int] = 0
    mat.print_matrix(hamming_result_11_15)

    hamming_parity_check_11_15 = mat.matrix_mult(hamming_result_11_15, hamming_11_15_H)
    row_length = len(hamming_parity_check_11_15[0])
    # print(row_length)

    for i in range(row_length):
        hamming_parity_check_11_15[0][i] %= 2
    
    hamming_parity_check_11_15[0].reverse()
    mat.print_matrix(hamming_parity_check_11_15)
