#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqrmtx = []
    if len(matrix) <= 0:
        return matrix
    else:
        for a in matrix:
            sqrmtx.append(list(map(lambda x: x * x, a)))
        return sqrmtx
