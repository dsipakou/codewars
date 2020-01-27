def max_gap(numbers):
    numbers.sort()
    max_gap = 0
    for i in range(len(numbers) - 1):
        max_gap = max(max_gap, numbers[i + 1] - numbers[i])
    return max_gap

print(max_gap([13,10,2,9,5]))
