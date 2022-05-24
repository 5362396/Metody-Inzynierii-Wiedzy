import numpy as np
import math as m


B = np.array([[1., 1., 1., 1., 1., 1., 1., 1.],
              [1., 1., 1., 1., -1., -1., -1., -1],
              [1., 1., -1., -1., 0., 0., 0., 0.],
              [0., 0., 0., 0., 1., 1., -1., -1.],
              [1., -1., 0., 0., 0., 0., 0., 0.],
              [0., 0., 1., -1., 0., 0., 0., 0.],
              [0., 0., 0., 0., 1., -1., 0., 0.],
              [0., 0., 0., 0., 0., 0., 1., -1.]])

# 1) Sprawdzić czy B ma wektory ortagonalne (B * B.T = macierz diagonalna)
diag = np.dot(B, B.T)
print(diag)

# 2) Znormalizować wektory w B (każdy wektor podzielić przez jego długość)
dlugosci = []
for wiersz in B:
    dlugosc = 0
    for liczba in wiersz:
        dlugosc += pow(liczba, 2)
    dlugosc = m.sqrt(dlugosc)
    dlugosci.append(dlugosc)

ortnrml = []
for wektor in range(len(B[0])):
    ortnrml.append(B[wektor] * (1 / dlugosci[wektor]))
ortnrml = np.array(ortnrml)
print(ortnrml)

# 3) Tak zmodyfikowaną B sprawdzić czy jest ortonormalna (B * B.T = macierz jednostkowa)
jedn = np.dot(ortnrml, ortnrml.T)
print(jedn)

# 4) Przeprowadzić wektor [8 6 2 3 4 6 6 5] z bazy standardowej do bazy B po normalizacji
v1 = np.array([8., 6., 2., 3., 4., 6., 6., 5.])
v2 = np.dot(ortnrml, v1)
print(v2)
