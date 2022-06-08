import math as m
import numpy as np

with open("../australian.dat", "r") as file:
    matrix = [list(map(lambda a: float(a), line.split())) for line in file]


def metryka_euklidesowa(l1, l2):
    suma = 0
    for i in range(len(l1) - 1):
        suma += (l1[i] - l2[i]) ** 2
    return m.sqrt(suma)


def odleglosc(x, lista):
    wynik = []
    for i in range(0, len(lista)):
        metryka = metryka_euklidesowa(lista[i], x)
        wynik.append((lista[i][len(lista[i])-1], metryka))
    return wynik


def grupowanie(lista):
    wynik = dict()
    for i in lista:
        decyzja = i[0]
        if decyzja in wynik.keys():
            wynik[decyzja].append(i[1])
        else:
            wynik[decyzja] = [i[1]]
    return wynik


def sasiedzi(k, slownik):
    lista = []
    for klucz in slownik.keys():
        slownik[klucz].sort()
        suma = 0
        for wartosc in range(k):
            suma += slownik[klucz][wartosc]
        lista.append(suma)
    if lista[0] < lista[1]:
        return 0
    else:
        return 1


x = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
zad1 = odleglosc(x, matrix)
print("Odległość")
print(zad1)
zad2 = grupowanie(zad1)
print("Grupowanie")
print(zad2)
zad3 = sasiedzi(2, zad2)
print("Decyzja")
print(zad3)


# mamy metryke euklidesową, robimy pierwiastek sumy kwadraków różnic
# metryke zrobić w oparciu o wektor i o dzialania na wektorze (matematycznym oczywiscie)


def metryka_euklidesowa_wektory(l1, l2, utnij):
    if utnij:
        l1 = l1[:-1]
        l2 = l2[:-1]
    v1 = np.array(l1)
    v2 = np.array(l2)
    c = v2 - v1
    return m.sqrt(np.dot(c, c))


print("\nPD")
print(metryka_euklidesowa_wektory(matrix[0], matrix[1], True))
print(metryka_euklidesowa_wektory(matrix[0], matrix[1], True) == metryka_euklidesowa(matrix[0], matrix[1]))
