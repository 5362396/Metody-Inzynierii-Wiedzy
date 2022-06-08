import math as m
import numpy as np

np.set_printoptions(formatter={'float_kind': "{:.7f}".format})


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


a = np.array([[1., 2., 0.], [2., 0., 2.]])
aat = np.dot(a, a.T)
ata = np.dot(a.T, a)
wartosci_wlasne_aat = wartosci_wlasne(aat)
wartosci_wlasne_ata = np.sort(np.linalg.eig(ata)[0])[::-1]

s = np.zeros((2, 3))
s_temp = np.diag([m.sqrt(i) for i in wartosci_wlasne_aat])
for i in range(len(s_temp[0])):
    for j in range(len(s_temp[1])):
        s[i][j] = s_temp[i][j]

v = []
for i in range(len(ata[0])):
    wektor_v = []
    for j in range(len(ata[0]), 0, -1):
        wektor_v.append(np.linalg.eigh(ata)[1][i][j-1])
    v.append(wektor_v)
v = np.array(v)

u = []
for i in range(len(aat[0])):
    u.append(np.dot(a, v.T[i]) * (1 / m.sqrt(wartosci_wlasne_aat[i])))
u = np.array(u)

print("WARTOŚCI WŁASNE U")
print(wartosci_wlasne_aat)
print("WARTOŚCI WŁASNE V")
print(wartosci_wlasne_ata)
print("MACIERZ U")
print(u)
print("WARTOŚCI SINGULARNE")
print(s)
print("MACIERZ V TRANSPONOWANE")
print(v.T)
print("SPRAWDZENIE")
print(np.dot(np.dot(u, s), v.T))
