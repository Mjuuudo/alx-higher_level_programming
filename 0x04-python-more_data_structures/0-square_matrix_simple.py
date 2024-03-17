#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    new_matrix = map(lambda x: x ** x, matrix)
    squared_list = list(new_matrix)
    return new_matrix

