def minimum(a, x):
    return min(a % x, x - a % x)

print(minimum(11, 6))
