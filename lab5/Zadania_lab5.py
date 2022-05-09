import math as m
import numpy as np
import random

with open("../australian.dat", "r") as file:
    matrix = [list(map(lambda a: float(a), line.split())) for line in file]
file.close()


def metryka_euklidesowa(l1, l2):
    suma = 0
    for i in range(len(l1) - 1):
        suma += (l1[i] - l2[i]) ** 2
    return m.sqrt(suma)


def odleglosc(x, lista):
    wynik = []
    for i in range(0, len(lista)):
        metryka = metryka_euklidesowa(lista[i], x)
        wynik.append((lista[i][len(lista[i]) - 1], metryka))
    return wynik


# lab5
# zad1 - 28 luty 1h 10min wykład tresc zadania (kolorowanie -> środek masy -> kolorowanie ...)


def losowe_wartosci(lista):
    wynik = []
    for i in lista:
        wynik.append(i)
    for j in range(len(wynik)):
        wynik[j][-1] = float(random.randint(0, 1))  # to zmieniać w razie większej ilości "kolorów"
    return wynik


def srodek_masy(lista, indexy):
    odleglosci = []
    suma_odleglosci = 0

    for i in indexy:
        for j in indexy:
            suma_odleglosci += metryka_euklidesowa(lista[i], lista[j])
        odleglosci.append(suma_odleglosci)
        suma_odleglosci = 0

    najmniejszy = 0
    for k in range(1, len(odleglosci)):
        if odleglosci[k] < odleglosci[najmniejszy]:
            najmniejszy = k
    return najmniejszy


def kolorowanie(lista):
    zmiany_srodkow = True
    while zmiany_srodkow:
        zmiany_srodkow = False
        grupy = dict()
        for i in range(len(lista)):
            decyzja = lista[i][-1]
            if decyzja in grupy.keys():
                grupy[decyzja].append(i)
            else:
                grupy[decyzja] = [i]

        lista_wartosci = []
        for j in grupy.values():
            lista_wartosci += j

        lista_srodkow = []
        for k in grupy.values():
            lista_srodkow.append(k[srodek_masy(lista, k)])

        lista_odleglosci = []
        for wartosc in lista_wartosci:
            for srodek in lista_srodkow:
                lista_odleglosci.append(metryka_euklidesowa(lista[wartosc], lista[srodek]))

            najmniejszy = 0
            ilosc_najmniejszych = 1
            for i in range(1, len(lista_odleglosci)):
                if lista_odleglosci[najmniejszy] > lista_odleglosci[i]:
                    najmniejszy = i
                    ilosc_najmniejszych = 1
                elif lista_odleglosci[najmniejszy] == lista_odleglosci[i]:
                    ilosc_najmniejszych = ilosc_najmniejszych + 1
            if ilosc_najmniejszych == 1:
                if lista[wartosc][-1] != lista[lista_srodkow[najmniejszy]][-1]:
                    lista[wartosc][-1] = lista[lista_srodkow[najmniejszy]][-1]
                    zmiany_srodkow = True
            elif ilosc_najmniejszych > 1:
                lista[wartosc][-1] = None
                zmiany_srodkow = True
            lista_odleglosci = []
        # print(lista_srodkow)
    return lista


def porownanie(lista1, lista2):
    ilosc_roznic = 0
    for i in range(len(lista1)):
        if lista1[i] != lista2[i]:
            ilosc_roznic = ilosc_roznic + 1
    print("Ilość różniących się wierszy: " + str(ilosc_roznic))
    print(str((len(lista1) - ilosc_roznic) / len(lista1) * 100) + "% danych identycznych do oryginalnych")


# losowe = losowe_wartosci(matrix)
# with open("../australian.dat", "r") as file:
#     matrix = [list(map(lambda a: float(a), line.split())) for line in file]
# porownanie(matrix, losowe)
# pokolorowane = kolorowanie(losowe)
# porownanie(matrix, pokolorowane)


# zad2 - calkowanie numeryczne (metoda montecarlo)
def f(x):
    return x ** 2


def f2(x):
    return x ** 3 / 3


def montecarlo(ilosc_punktow, xk, xp):
    traf = 0
    dx = np.abs(xk - xp)
    for i in range(ilosc_punktow):
        x = xp + np.random.random() * (abs(xp - xk))
        traf += f(x)
    wynik = dx * traf / ilosc_punktow
    return wynik


def calkowanie_montecarlo(ilosc_wywolan):
    for j in range(ilosc_wywolan):
        xp = np.random.randint(-100, 100)
        xk = np.random.randint(-100, 100)
        xp, xk = sorted([xp, xk])
        print("*******************" + str(j + 1) + "*******************")

        lista = [10, 100, 1000, 10000, 100000]
        for i in lista:
            print("Ilość punktów: " + str(i))
            numerycznie = montecarlo(i, xk, xp)
            rzeczywista = f2(xk) - f2(xp)
            print("xp={:=3d} xk={:=3d} rzeczywista={:>10.2f} numerycznie={:>10.2f} błąd={:>11.8f}%"
                  .format(xp, xk, rzeczywista, numerycznie, 100 * (rzeczywista - numerycznie) / rzeczywista))


print("xp - początek całkowania, xk - koniec całkowania")
# calkowanie_montecarlo(1)


# zad3 - calkowanie numeryczne 2 (podzial na duzo prostokatow)
def prostokaty(xp, xk, i):
    dx = (xk - xp) / i
    wynik = 0
    for x in range(i):
        x = x * dx + xp
        wynik += dx * f(x)
    return wynik


def calkowanie_prostokaty(ilosc_wywolan):
    for j in range(ilosc_wywolan):
        xp = np.random.randint(-100, 100)
        xk = np.random.randint(-100, 100)
        xp, xk = sorted([xp, xk])
        print("*******************" + str(j + 1) + "*******************")

        lista = [10, 100, 1000, 10000, 100000]
        for i in lista:
            print("Ilość podprzedziałów (prostokątów): " + str(i))
            numerycznie = prostokaty(xp, xk, i)
            rzeczywista = f2(xk) - f2(xp)
            print("xp={:=3d} xk={:=3d} rzeczywista={:>10.2f} numerycznie={:>10.2f} błąd={:>11.8f}%"
                  .format(xp, xk, rzeczywista, numerycznie, 100 * (rzeczywista - numerycznie) / rzeczywista))


# calkowanie_prostokaty(1)
