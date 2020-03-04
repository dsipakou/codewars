def product(prod):
    f1 = 0
    f2 = 1
    while f1 * f2 < prod:
        f1, f2 = f2, f1 + f2
    if f1 * f2 == prod:
        return [f1, f2, True]
    return [f1, f2, False]

print(product(4895))
