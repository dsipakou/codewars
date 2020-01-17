def seq(n):
    if n < 2 and n >= 0:
        return f"{n}={n}"
    if n < 0:
        return f"{n}<0"
    output = '+'.join(str(s) for s in range(n + 1))
    if n % 2 == 0:
        num = (n + 1) * (n // 2)
        return f"{output} = {num}"
    else:
        num = (n) * ((n - 1) // 2) + n
        return f"{output} = {num}"

print(seq(11))
