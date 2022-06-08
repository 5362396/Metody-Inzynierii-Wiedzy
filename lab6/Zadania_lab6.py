import math as m
import numpy as np


def srednia_arytmetyczna(lista):
    return sum(lista) / len(lista)


def wariancja(lista):
    srednia = srednia_arytmetyczna(lista)
    suma = 0.0
    for i in lista:
        suma += (i - srednia) ** 2
    return float(suma / (float(len(lista))))


def odchylenie_standardowe(lista):
    return m.sqrt(wariancja(lista))


def srednia_arytmetyczna_wektorowo(lista):
    wektor_jednostkowy = np.ones((len(lista), 1))
    return float(np.dot(np.array(lista), wektor_jednostkowy) / len(lista))


def wariancja_wektorowo(lista):
    srednia = srednia_arytmetyczna_wektorowo(lista)
    wektor_jednostkowy = np.ones((len(lista), 1))
    srednia_wektor = wektor_jednostkowy * srednia
    odejmowanie = np.array(lista) - srednia_wektor
    return float(np.dot(odejmowanie[0], odejmowanie[1]) / len(lista))


def odchylenie_standardowe_wektorowo(lista):
    return m.sqrt(wariancja_wektorowo(lista))


listaa = [1, 5, 4, 10]

print("Średnia arytmetyczna: " + str(srednia_arytmetyczna(listaa)))
print("Wariancja: " + str(wariancja(listaa)))
print("Odchylenie standardowe: " + str(odchylenie_standardowe(listaa)))

print("Średnia arytmetyczna wektorowo: " + str(srednia_arytmetyczna_wektorowo(listaa)))
print("Wariancja wektorowo: " + str(wariancja_wektorowo(listaa)))
print("Odchylenie standardowe wektorowo: " + str(odchylenie_standardowe_wektorowo(listaa)))
