def contains_value(my_list: list, value: int) -> bool:
    return value in my_list


numbers = [1, 3, 5, 7, 9]
check_number = [1]
result = contains_value(numbers, check_number)
if result:
    print(f"Lista zawiera liczbę {check_number}")
else:
    print(f"Lista nie zawiera liczby {check_number}")
