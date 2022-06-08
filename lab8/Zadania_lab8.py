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


np.set_printoptions(formatter={'float_kind': "{:.7f}".format})
a = np.array([[2, 0], [1, 1], [0, 2]])

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

q = np.array(q).T
r = np.dot(q.T, a)
a_spr = np.dot(q, r)
print("Q")
print(q)
print("R")
print(r)
print("A")
print(a_spr)
