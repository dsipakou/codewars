def solve():
    a = 999
    b = 999
    max_prod = 0
    while a > 99 and b > 99:
        prod = a * b
        if str(prod) == str(prod)[::-1]:
            max_prod = max(max_prod, prod)
        if b == 100:
            b = 999
            a -= 1
        else:
            b -= 1
    return max_prod

print(solve())
