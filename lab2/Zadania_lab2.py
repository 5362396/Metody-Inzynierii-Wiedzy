haslo = "dmk!#31MSpj"

if len(haslo) > 9:
    male = 0
    duze = 0
    spec = 0
    for i in range(len(haslo)):
        if haslo[i].islower():
            male += 1
        if haslo[i].isupper():
            duze += 1
        if not haslo[i].isalnum():
            spec += 1
    if male > 0 and duze > 0 and spec > 0:
        print("Haslo silne, brawo!")
    else:
        print("Haslo nie spelnia wymagan odnosnie malych, duzych liter oraz znakow specjalnych.")
else:
    print("Haslo bardzo slabe, mniej niz 10 znakow.")

lista_liczb = [4, 2, 67, 99, 1]
for i in range(len(lista_liczb)):
    if lista_liczb[i] == 99:
        continue
    else:
        print(lista_liczb[i])


def czyNalezy(liczba, lista):
    i = 0
    wynik = False
    while i < len(lista):
        if liczba == lista[i]:
            wynik = True
            break
        i += 1
    return wynik


print(czyNalezy(1, lista_liczb))

with open("plik.txt") as plik:
    lines = plik.readlines()
    for i in lines:
        print(i, end="")

lista_stringow = ["python", "c", "cpp", "java", "prolog"]
plik2 = open("plik2.txt", "w")
for j in lista_stringow:
    print(j, file=plik2)
plik2.close()
print("")

miasta = ["Olsztyn", "Warszawa", "Kraków", "Łódź"]
result = map(lambda x: x[:3], miasta)
print(list(result))

lista_plikow = ["tekstowy.txt, word.docx, pyton.py, hasla.txt, skrypt.exe"]


def x(lista, ext):
    for i in lista:
        if i.endswith(ext):
            yield i


test = x(lista_plikow, ".txt")
print(list(test))
