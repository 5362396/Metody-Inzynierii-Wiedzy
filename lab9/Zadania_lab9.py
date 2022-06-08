import math as m
import numpy as np


def projekcja(u, V):
    V_u = np.dot(V.T, u)
    u_u = np.dot(u.T, u)
    if u_u == 0:
        return u
    return (V_u / u_u) * u


def dlugosc_wektora(u):
    return m.sqrt(np.dot(u.T, u))


def macierz_q(a):
    v_list = [[x[i] for x in a] for i in range(len(a[1]))]
    u_list = []
    q = []

    for v in v_list:
        v = np.array(v)
        suma_projekcji = 0
        for u_i in u_list:
            u_i = np.array(u_i)
            suma_projekcji += projekcja(u_i, v)
        u = v - suma_projekcji
        u_list.append(u)
        if dlugosc_wektora(u) != 0:
            e = u * (1 / dlugosc_wektora(u))
        else:
            e = u
        q.append(e)

    return np.array(q).T


def rekurencja_a(a):
    q = macierz_q(a)
    a2 = np.dot(q.T, a)
    a2 = np.dot(a2, q)
    return a2


def wartosci_wlasne(a):
    a3 = a
    dim = len(a3[0])
    while (np.diag(a3) - np.dot(a3, np.ones((dim, 1))).T).all() > 0.001:
        a3 = rekurencja_a(a3)
    return np.diag(a3)


a = np.array([[2., 1., 3., 7.], [1., 6., 6., 6.], [3., 6., 1., 2.], [7., 6., 2., 3.]])
print("A:")
print(a)
print("\n")
wynik = wartosci_wlasne(a)
print("\n")
# https://matrixcalc.org/pl/vectors.html#eigenvectors(%7B%7B2,1,3,7%7D,%7B1,6,6,6%7D,%7B3,6,1,2%7D,%7B7,6,2,3%7D%7D)
# lambda1 = 16,070 lambda2 = -6,668 lambda3 = 3,937 lambda4 = -1,339
print("WYNIK:", wynik)
print("\n")
