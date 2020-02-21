def zero_sum(n):
    if n == 1:
        return [0]
    output = []
    for i in range((n - n % 2) // 2 - 1):
        output.extend([-5 - i, 5 + i])
    if n % 2 == 1:
        output.extend([3, -1, -2])
    else:
        output.extend([-2, 2])
    return output
print(zero_sum(6))
