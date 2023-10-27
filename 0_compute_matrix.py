#!/usr/bin/python3

import sys

def compute_matrix(matrix=[]):
    
    def square(x):
        return x * x

    return list(map(lambda row: list(map(square, row)), matrix))


if __name__ == '__main__':
    matrix = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]

    print(f'Original: {matrix}')
    print(f'Modified: {compute_matrix(matrix)}')
