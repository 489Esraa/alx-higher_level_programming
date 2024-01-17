#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    if matrix is None:
        return
    if len(matrix) == 0:
        print()
    else:
        for arr in new_matrix:
            for el in range(0, len(arr)):
                m = arr[el] * arr[el]
                print("{:d}".format(m), end="")
                if el != len(arr) - 1:
                    print(end=" ")
            print()
