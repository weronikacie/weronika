def combine_and_cube(list1: list, list2: list) -> list:
    combined = list(set(list1 + list2))
    cubed = [x**3 for x in combined]
    return cubed


list1 = [2, 3, 4]
list2 = [5, 6, 7]

result = combine_and_cube(list1, list2)
print(result)
