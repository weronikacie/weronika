def wypisz_parzyste(lista):
    for liczba in lista:
        if liczba % 2 == 0:
            print(liczba)
lista = list(range(10))
wypisz_parzyste(lista)
