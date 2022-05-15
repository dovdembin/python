import numpy as np
from numpy.random import random

import matplotlib.pyplot as plt
from scipy import misc  # contains an image of a racoon!
from PIL import Image  # for reading image files


def Dimension_1():
    ############## 1-Dimension ###############
    my_array = np.array([1.1, 9.2, 8.1, 4.1])
    print(my_array.shape)
    # accessing
    print(my_array[2])
    # show shape
    print(my_array.shape)
    # show dimension
    print(my_array.ndim)


def Dimension_2():
    ############# 2-Dimensions ####################
    array_2d = np.array([
        [1, 2, 3, 9],
        [5, 6, 7, 8]
    ])
    print(f'array_2d has {array_2d.ndim} dimensions')
    print(f'Its shape is {array_2d.shape}')
    print(f'It has {array_2d.shape[0]} rows and {array_2d.shape[1]} columns')
    print(array_2d)
    # To access
    print(array_2d[1, 2])
    # To access an entire row
    print(array_2d[0, :])
    # Access the 3rd value
    print(f"value is {array_2d[1, 2]}")


def Dimension_N():
    ############# N-Dimensions ####################
    mystery_array = np.array([
        [[0, 1, 2, 3],
         [4, 5, 6, 7]],

        [[7, 86, 6, 98],
         [5, 1, 0, 4]],

        [[5, 36, 32, 48],
         [97, 0, 27, 18]]
    ])

    print(f'We have {mystery_array.ndim} dimensions')
    print(f'The shape is {mystery_array.shape}')
    print(mystery_array[2, 1, 3])
    # print row
    print(mystery_array[2, 1, :])
    print(mystery_array[:, 0, 0])


def arange_():
    # Return evenly spaced values within a given interval.
    a = np.arange(10, 30)
    return a


def print_example():
    a = arange_()
    print(a)
    print(a[-3:])  # The last 3 values in the array
    print(a[3:6])  # An interval between two values
    print(a[12:])  # All the values except the first 12
    print(a[::2])  # Every second value
    print(a[::-1])  # reverse the order of an array
    print(np.flip(a))  # reverse the order of an array


def nonzero_():
    # Print out all the indices of the non-zero elements in this array
    b = np.array([6, 0, 9, 0, 0, 5, 0])
    nz_indices = np.nonzero(b)
    nz_indices  # note this is a tuple
    print(nz_indices)


def random_():
    z = random((3, 3, 3))  # or use the full path to call it z = np.random.random((3,3,3))
    print(z)
    print(z[2, 2, 1])


def linspace_():
    x = np.linspace(0, 100, num=9)
    print(x.shape)
    print(x)


def add_multiply_array():
    v1 = np.array([4, 5, 2, 7])
    v2 = np.array([2, 1, 3, 3])
    print(v1 + v2)
    print(v1 * v2)


def broadcasting_():
    array_2d = np.array([[1, 2, 3, 4],
                         [5, 6, 7, 8]])

    print(array_2d + 10)
    print(array_2d * 5)


def matrix_multiplication():
    a1 = np.array([[1, 3],
                   [0, 1],
                   [6, 2],
                   [9, 7]])

    b1 = np.array([[4, 1, 3],
                   [5, 8, 5]])

    c = np.matmul(a1, b1)
    print(f'Matrix c has {c.shape[0]} rows and {c.shape[1]} columns.')
    print(c)
    print(a1 @ b1)


def flip_and_rot90():
    a1 = np.array([[1, 3],
                   [0, 1],
                   [6, 2],
                   [9, 7]])
    print(np.flip(a1))
    print(np.rot90(a1))


def compare2booleanarrays():
    bool_list1 = [True, True, False, False]
    bool_list2 = [False, True, True, False]
    print(np.array(bool_list1) & np.array(bool_list2))


if __name__ == "__main__":
    compare2booleanarrays()
