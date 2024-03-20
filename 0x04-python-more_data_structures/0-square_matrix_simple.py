#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for rows in matrix:
            new_matrix.append([columns * columns for columns in rows])
    return (new_matrix)
    

