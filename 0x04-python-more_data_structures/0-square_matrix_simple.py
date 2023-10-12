#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for k in matrix:
        new_row = []
        for j in range(0, len(k)):
            new_row.append(k[j] * k[j])
        new_matrix.append(new_row)

    return new_matrix