def check_sum(a: int, b: int, c: int) -> bool:
    return a + b == c
result = check_sum(5, 7, 10)
if result:
    print("Suma dwóch pierwszych liczb jest większa lub równa trzeciej")
else:
    print("Suma dwóch pierwszych liczb jest mniejsza od trzeciej")