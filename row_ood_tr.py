def fun(n):
    base = n ** 2 - n + 1
    return [base * (i + 1) for i in range(n)]

print(fun(5))
