def divisors(n):
    output = 0
    for i in range(n, 0, -1):
        if n % i == 0:
            output += 1
    return output
