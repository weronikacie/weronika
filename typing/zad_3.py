def is_even(number: int) -> bool:
    return number % 2 == 0


number_to_check = 9
even_check = is_even(number_to_check)
if even_check:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
