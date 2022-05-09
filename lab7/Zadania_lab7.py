import math as m
import numpy as np
import random


# (x, y) = (2, 1), (5, 2), (7, 3), (8, 3)
# B0 = 2/7
# B1 = 5/14
# ostatni wykład (04.04) 1h 22min


def macierz_kowariancji(matrix):
    return np.dot(matrix.T, matrix)


def odwrotnosc_macierzy(matrix):
    return np.linalg.inv(matrix)


def lewa_odwrotnosc(matrix):
    mk = macierz_kowariancji(matrix)
    odw = odwrotnosc_macierzy(mk)
    return np.dot(odw, matrix.T)


def regresja_liniowa(matrix):
    x = np.array([[1, x[0]] for x in matrix])
    y = np.array([x[1] for x in matrix])
    lewa_odw = lewa_odwrotnosc(x)
    return np.dot(lewa_odw, y)


B0 = 2/7
B1 = 5/14
print(B0)
print(B1)
x_y = np.array([[2, 1], [5, 2], [7, 3], [8, 3]])
print(regresja_liniowa(x_y))
