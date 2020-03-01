def per_rec(n):
    first = 1
    second = 1
    summ = first + second
    for i in range(2, n):
        first, second = second, first+second
        summ += second
    return summ * 4

def helper(n, d):
    if n not in d:
        d[n] = helper(n - 1, d) + helper(n - 2, d)
    return d[n]

print(per_rec(8))
