#!/usr/bin/python3

"""
This Python program is inspired from implementing the logic behind matrix
multiplication as found on the Wikipedia site:
https://en.wikipedia.org/wiki/Matrix_multiplication#
"""

from math import floor, log10

def matrix_mult(_matrix_a, _matrix_b) -> list:
    matrix_c = [ [0] * len(_matrix_b[0]) for _ in range(len(_matrix_a))]
    # print_matrix(matrix_c)
    for y in range(len(_matrix_a)):
        for x in range(len(_matrix_b[0])):
            for z in range(len(_matrix_a[0])):
                matrix_c[y][x] += _matrix_a[y][z] * _matrix_b[z][x]
    return matrix_c

def largest_in_col(_matrix, _col):
    neg = False
    largest = 0
    for row in _matrix:
        if abs(row[_col]) > largest:
            largest = abs(row[_col])
        if row[_col] < 0:
            neg = True
    return largest, neg

def print_matrix(_matrix, places=0):
    neg = False
    for row in _matrix:
        print('|', end=' ')
        for x in range(len(row)):
            largest, neg = largest_in_col(_matrix, x)
            if neg:
                fmt_str = '{: .' +str(places) + 'f}'
            else:
                fmt_str = '{:.' +str(places) + 'f}'
            largest = round(largest, places) if round(largest, places) != 0.0 else 1
            row[x] = round(row[x], places) if round(row[x], places) != 0.0 else abs(round(row[x], places))
            value = round(row[x], places) if round(row[x], places) != 0.0 else 1    # log10(num), where num is not zero
            end = ' ' * (floor(log10(abs(largest))) - floor(log10(abs(value))) + 1)
            num = fmt_str.format(row[x])
            print(num, end=end)
        print('|')

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
    print_matrix(matrix_B)
    
    matrix_C = matrix_mult(matrix_A, matrix_B)
    print_matrix(matrix_C)
    
    matrix_D = [
        [100],
        [80],
        [60]
    ]
    print_matrix(matrix_D)
    
    matrix_E = matrix_mult(matrix_C, matrix_D)
    print_matrix(matrix_E)


    matrix_F = [
        [4, 7],
        [2, 6]
    ]

    matrix_G = [
        [0.6, -0.7],
        [-0.2, 0.4]
    ]

    matrix_H = matrix_mult(matrix_F, matrix_G)
    # print(matrix_H)
    print_matrix(matrix_H)

    matrix_A_trsnsposed = transpose_matrix(matrix_A)
    print_matrix(matrix_A)
    print_matrix(matrix_A_trsnsposed)
