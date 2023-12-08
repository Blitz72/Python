#!/usr/bin/python3

"""
This Python program is inspired from implementing the logic behind matrix
multiplication as found on the Wikipedia site:
https://en.wikipedia.org/wiki/Matrix_multiplication#
"""

from math import floor, log10

def largest_in_col(_matrix, _col, _places):
    neg = False
    largest = 0
    for row in _matrix:
        if abs(row[_col]) > largest:
            largest = abs(row[_col])
        if round(row[_col], _places) < 0:
            neg = True
    return largest, neg

def print_matrix(_matrix, _places=0):
    largest_dict = {}
    for col in range(len(_matrix[0])):
        largest_dict[col] = {}
        largest_dict[col]['largest'], largest_dict[col]['neg'] = largest_in_col(_matrix, col, _places)
    for row in _matrix:
        print('|', end=' ')
        for col in range(len(row)):
            largest = largest_dict[col]['largest']
            neg = largest_dict[col]['neg']
            largest = round(largest, _places) if round(largest, _places) != 0.0 else 1
            value_to_print = round(row[col], _places) if round(row[col], _places) != 0.0 else abs(round(row[col], _places))
            value_for_end = round(row[col], _places) if round(row[col], _places) != 0.0 else 1    # log10(num), where num is not zero
            end = ' ' * (floor(log10(abs(largest))) - floor(log10(abs(value_for_end))) + 1) if isinstance(value_for_end, int) else ' '
            fmt_str = '{: .' +str(_places) + 'f}' if neg else '{:.' +str(_places) + 'f}'
            num = fmt_str.format(value_to_print)
            print(num, end=end)
        print('|')

def mult_matrix(_matrix_a, _matrix_b) -> list:
    matrix_c = [ [0] * len(_matrix_b[0]) for _ in range(len(_matrix_a))]
    # print_matrix(matrix_c)
    for y in range(len(_matrix_a)):
        for x in range(len(_matrix_b[0])):
            for z in range(len(_matrix_a[0])):
                matrix_c[y][x] += _matrix_a[y][z] * _matrix_b[z][x]
    return matrix_c

def transpose_matrix(_matrix) -> list:
    matrix_transposed = [[0 for _ in range(len(_matrix))] for _ in range(len(_matrix[0]))]
    for j in range(len(_matrix)):
        for i in range(len(_matrix[0])):
            matrix_transposed[i][j] = _matrix[j][i]
    return matrix_transposed

if __name__ == "__main__":
    matrix_A = [
        [1, 0, 1],
        [2, 1, 1],
        [0, 1, 1],
        [1, 1, 2],
    ]
    matrix_B = [
        [1, 2, 1],
        [2, -3, 1],
        [4, 2, 2]
    ]
    print_matrix(matrix_A)
    print()
    print_matrix(matrix_B)
    print()

    matrix_C = mult_matrix(matrix_A, matrix_B)
    print_matrix(matrix_C)
    print()
    
    matrix_D = [
        [100],
        [80],
        [60]
    ]
    print_matrix(matrix_D)
    print()
    
    matrix_E = mult_matrix(matrix_C, matrix_D)
    print_matrix(matrix_E)
    print()

    matrix_F = [
        [4, 7],
        [2, 6]
    ]

    matrix_G = [
        [0.6, -0.7],
        [-0.2, 0.4]
    ]

    matrix_H = [
        [1.23, 4.56],
        [7.89, 10.11]
    ]

    matrix_I = mult_matrix(matrix_F, matrix_G)
    print(matrix_I)
    print_matrix(matrix_I, _places=20)
    print()
    print_matrix(matrix_I, _places=0)
    print(matrix_I)
    print()

    matrix_J = mult_matrix(matrix_G, matrix_H)
    # print(matrix_J)
    print_matrix(matrix_J, _places=4)
    print()

    print_matrix(transpose_matrix(matrix_J), _places=4)
    print()

    matrix_A_trsnsposed = transpose_matrix(matrix_A)
    print_matrix(matrix_A)
    print()
    print_matrix(matrix_A_trsnsposed)
    print()
