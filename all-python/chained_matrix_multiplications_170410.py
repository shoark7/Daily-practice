"""Get least number of multiplications of chained matrix.

This is from our algorithm class in school.
It's really short, but very impressive.
Considering matrix dimensions as arrays of row and columns is really,
really awesome.
You can try too.

Start date: 2017/04/10
End date  : 2017/04/10
"""

import math


def least_matrix_multiplications(dims):
    """Get the number of matrix multiplications as few as possible.

    Each element is a sequence of a serial matrix.
    [10, 20, 30] means 10x20, 20x30 matrixs' multiplications.

    :input:
        dims: dimensions. rows and columns of matrix in a list.
    :return:
        number_of_multiplications. Least of the given.
    """

    size = len(dims) - 1
    matrix = [[0 for _ in range(size)] for _ in range(size)]

    for mul_depth in range(1, size):
        for i in range(size - mul_depth):
            j = i + mul_depth
            matrix[i][j] = math.inf

            for k in range(i, j):
                temp = matrix[i][k] + matrix[k+1][j] + dims[i] * dims[k+1] * dims[j+1]
                if temp < matrix[i][j]:
                    matrix[i][j] = temp

    return matrix[0][size-1]
