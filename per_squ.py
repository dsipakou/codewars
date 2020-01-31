def num_sq(n):
    output = [float('inf') for _ in range(n + 1)]
    output[0] = 0
    i = tmp = 1
    while tmp <= n:
        for j in range(tmp, len(output)):
            output[j] = min(output[j], output[j - tmp] + 1)
        i += 1
        tmp = i**2
    return output[-1]

print(num_sq(13))
