def greet(name: str, surname: str) -> str:
    return f"Cześć {name} {surname}!"

result = greet("Weronika", "Cieslak")

print(result)


def multiply(a: int, b: int) -> int:
    return a * b

result = multiply(5, 7)
print(result)


def is_even(number: int) -> bool:
    return number % 2 == 0
number_to_check = 9
even_check = is_even(number_to_check)
if even_check:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")

def check_sum(a: int, b: int, c: int) -> bool:
    return a + b == c
result = check_sum(5, 7, 10)
if result:
    print("Suma dwóch pierwszych liczb jest większa lub równa trzeciej")
else:
    print("Suma dwóch pierwszych liczb jest mniejsza od trzeciej")

def contains_value(my_list: list, value:int) -> bool:
    return value in my_list
numbers = [1, 3, 5, 7, 9]
check_number = [1]
result = contains_value(numbers, check_number)
if result:
    print(f"Lista zawiera liczbę {check_number}")
else:
    print(f"Lista nie zawiera liczby {check_number}")

def combine_and_cube(list1: list, list2: list) -> list:
    combined = list(set(list1 + list2))
    cubed = [x ** 3 for x in combined]
    return cubed

list1 = [2,3,4]
list2 = [5,6,7]

result = combine_and_cube(list1, list2)
print(result)

