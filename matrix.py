#!/usr/bin/python3

matrix_A = [
    [1, 0, 1],
    [2, 1, 1],
    [0, 1, 1],
    [1, 1, 2],
]
matrix_B = [
    [1, 2, 1],
    [2, 3, 1],
    [4, 2, 2]
]

def matrix_mult(matrix_a, matrix_b):
    matrix_c = [ [0] * len(matrix_b[0]) for _ in range(len(matrix_a))]
    # print_matrix(matrix_c)
    for y in range(len(matrix_a)):
        for x in range(len(matrix_b[0])):
            for z in range(len(matrix_a[0])):
                matrix_c[y][x] += matrix_a[y][z] * matrix_b[z][x]
    return matrix_c

def largest_in_col(matrix, col):
    neg = False
    largest = 0
    for row in matrix:
        if abs(row[col]) > largest:
            largest = abs(row[col])
        if row[col] < 0:
            neg = True
    return largest, neg

def print_matrix(matrix, places=0):
    from math import floor, log10
    neg = False
    for row in matrix:
        print('|', end=' ')
        for x in range(len(row)):
            largest, neg = largest_in_col(matrix, x)
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
    print()

if __name__ == "__main__":
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
