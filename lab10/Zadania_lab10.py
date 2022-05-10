import numpy as np


def gauss_jordan_rownania(ilosc_niewiadomych, macierz):
    wynik = np.zeros(ilosc_niewiadomych)
    for i in range(ilosc_niewiadomych):
        if not macierz[i][i] == 0.0:
            for j in range(ilosc_niewiadomych):
                if i != j:
                    wsp = macierz[j][i] / macierz[i][i]
                    for k in range(ilosc_niewiadomych + 1):
                        macierz[j][k] = macierz[j][k] - wsp * macierz[i][k]
        else:
            print("Nie można dzielić przez 0")
            return 0
    for k in range(ilosc_niewiadomych):
        wynik[k] = macierz[k][ilosc_niewiadomych] / macierz[k][k]
    return wynik


def gauss_jordan_macierz(stopien_macierzy, macierz):
    macierz2 = np.zeros((stopien_macierzy, 2 * stopien_macierzy))
    wynik = np.zeros((stopien_macierzy, stopien_macierzy))
    for i in range(stopien_macierzy):
        for j in range(stopien_macierzy):
            macierz2[i][j] = macierz[i][j]
    for i in range(stopien_macierzy):
        for j in range(stopien_macierzy):
            if i == j:
                macierz2[i][j + stopien_macierzy] = 1
    for i in range(stopien_macierzy):
        if not macierz2[i][i] == 0.0:
            for j in range(stopien_macierzy):
                if i != j:
                    wsp = macierz2[j][i] / macierz2[i][i]
                    for k in range(stopien_macierzy * 2):
                        macierz2[j][k] = macierz2[j][k] - wsp * macierz2[i][k]
        else:
            print("Nie można dzielić przez 0")
            return 0
    for i in range(stopien_macierzy):
        dzielnik = macierz2[i][i]
        for j in range(2 * stopien_macierzy):
            macierz2[i][j] = macierz2[i][j] / dzielnik
    for i in range(stopien_macierzy):
        for j in range(stopien_macierzy):
            wynik[i][j] = macierz2[i][j + stopien_macierzy]
    return wynik


# x = -3 y = 1 z = 4
macierz1 = np.array([[2., 1., 3., 7.], [6., 6., 6., 12.], [3., 5., 2., 4.]])
macierz2 = np.array([[1., 2., 3., 4.], [5., 6., 7., 8.], [9., 10., 11., 12.]])
macierz3 = np.array([[2., 2., 2.], [1., 3., 2.]])
# https://www.naukowiec.org/wiedza/matematyka/metoda-gaussa-jordana_622.html
macierz4 = np.array([[2., 1., 1., 1.], [5., 2., 2., 1.], [2., 1., 3., 0.], [1., 1., 2., 1.]])
print(gauss_jordan_rownania(3, macierz1))
print(gauss_jordan_rownania(3, macierz2))
print(gauss_jordan_rownania(2, macierz3))
print(gauss_jordan_macierz(4, macierz4))
