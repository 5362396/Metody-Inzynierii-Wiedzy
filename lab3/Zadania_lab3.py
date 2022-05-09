import math as m

miasta = ["Warszawa", "Gdańsk", "Łódź", "Poznań", "Ełk", "Sosnowiec"]

print(list(map(lambda a: a[0:3], miasta)))

with open("../australian.dat", "r") as file:
    matrix = [list(map(lambda a: float(a), line.split())) for line in file]


def metryka_euklidesowa(l1, l2):
    suma = 0
    for i in range(len(l1) - 1):
        suma += (l1[i] - l2[i]) ** 2
    return m.sqrt(suma)


print(metryka_euklidesowa(matrix[0], matrix[1]))
print(metryka_euklidesowa(matrix[0], matrix[2]))


# PD
# Funkcja licząca odległość pierwszego elementu listy dwuwymiarowej z pozostałymi jej elementami.
# Odległości pogrupować względem klasy decyzyjnej,(ostatni element listy) i przechowywać w słowniku
# gdzie kluczem jest wartość decyzyjna, a wartość listą zawierającą odległości.
# Czyli obliczyć odległość między y a x (y=lista[0], x należy do listy bez zerowego indexu).

def domowa(lista, index_decyzyjna):
    grupy = dict()
    y = lista[0]
    for x in range(1, len(lista)):
        decyzyjna = lista[x][index_decyzyjna]
        if decyzyjna in grupy.keys():
            grupy[decyzyjna].append(metryka_euklidesowa(y, lista[x]))
        else:
            grupy[decyzyjna] = [metryka_euklidesowa(y, lista[x])]
    return grupy


print("pracka domowa")
print(domowa(matrix, 14))
