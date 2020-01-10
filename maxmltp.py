def max_multiple(divisor, bound):
    i = bound
    while i > 0:
        if i % divisor == 0:
            return i
        i -= 1

print(max_multiple(2, 7))
