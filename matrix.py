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
    largest = 0
    for row in matrix:
        if row[col] > largest:
            largest = row[col]
    return largest

def print_matrix(matrix):
    from math import floor, log10
    end = ' '
    for row in matrix:
        print('|', end=' ')
        for x in range(len(row)):
            largest = largest_in_col(matrix, x)
            largest = largest if largest != 0 else 1
            row[x] = round(row[x], 1) if round(row[x], 1) != 0.0 else abs(round(row[x], 1))
            value = row[x] if row[x] != 0 else 1    # log10(num), where num is not zero
            end = ' ' * (floor(log10(largest)) - floor(log10(value)) + 1) 
            print(row[x], end=end)
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
