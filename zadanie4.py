def wypisz_co_drugi(lista):
    for i in range(0, len(lista), 2):
        print(lista[i])
lista = list(range(10))
wypisz_co_drugi(lista)