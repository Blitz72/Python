#!/usr/bin/python3

def calculate_attributes(_hamming_bit_depth):
    parity_bit_indices = []
    for x in range(_hamming_bit_depth):
        if 2**x > _hamming_bit_depth:
            cols = _hamming_bit_depth - x
            break
        parity_bit_indices.append(2**x - 1)
    
    return cols, parity_bit_indices

def build_hamming_matrices(_hamming_bit_depth):
    rows = _hamming_bit_depth
    cols, parity_bit_indices = calculate_attributes(_hamming_bit_depth)

    parity_check_matrix = [[0 for _ in range(rows)] for _ in range(rows - cols)]
    for j in range(len(parity_check_matrix)):
        new_row = []
        while len(new_row) < len(parity_check_matrix[0]) + 1:
            for _ in range(2**j):
                new_row.append(0)
            for _ in range(2**j):
                new_row.append(1)
        for i in range(len(parity_check_matrix[0])):
            parity_check_matrix[j][i] = new_row[i + 1]

    generator_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    index = 0
    parity_check_matrix_row = 0
    for j in range(rows):
        if j not in parity_bit_indices:
            generator_matrix[j][index] = 1
            index += 1
            if index > cols:
                index = cols
        else:
            check_row = []
            for x in range(len(parity_check_matrix[0])):
                if x not in parity_bit_indices:
                    if  parity_check_matrix[parity_check_matrix_row][x] == 1:
                        check_row.append(1)
                    else:
                        check_row.append(0)
            for i in range (cols):
                generator_matrix[j][i] = check_row[i]
            parity_check_matrix_row += 1

    return generator_matrix, parity_check_matrix


if __name__ == '__main__':
    import matrix as mat
    # from Hamming_matrix import hamming_15_11_G

    hamming_bit_depth = 7

    generator_matrix, parity_check_matrix = build_hamming_matrices(hamming_bit_depth)
    mat.print_matrix(generator_matrix)
    # print(generator_matrix == hamming_15_11_G)
    print()
    mat.print_matrix(parity_check_matrix)
    print()