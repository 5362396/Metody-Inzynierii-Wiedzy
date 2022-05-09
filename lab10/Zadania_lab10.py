import numpy as np


def gauss_jordan(ilosc_niewiadomych, macierz):
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


ilosc2 = 2
ilosc3 = 3
# x = -3 y = 1 z = 4
macierz1 = np.array([[2., 1., 3., 7.], [6., 6., 6., 12.], [3., 5., 2., 4.]])
macierz2 = np.array([[1., 2., 3., 4.], [5., 6., 7., 8.], [9., 10., 11., 12.]])
macierz3 = np.array([[2., 2., 2.], [1., 3., 2.]])
print(gauss_jordan(ilosc3, macierz1))
print(gauss_jordan(ilosc3, macierz2))
print(gauss_jordan(ilosc2, macierz3))
