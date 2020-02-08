def min_sum(numbers):
    return sum([min(arr) for arr in numbers])

print(min_sum([[1,2,3], [3,4,5], [5,6,7]]))
