def pomnoz_przez_dwa_for(lista):
    wynik = []
    for element in lista:
        wynik.append(element * 2)
    return wynik
lista = [4, 5, 6, 8, 9]
print(pomnoz_przez_dwa_for(lista))
