def divisors(n):
    return sum(1 for i in range(n, 0, -1) if n % i == 0)


print(divisors(17))
