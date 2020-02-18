def fin(arr):
    i = 0
    while i < len(arr) - 1:
        if arr[i + 1] != arr[i] + 1:
            return arr[i + 1]
        i += 1
    return None

print(fin([1,2,3,5,6,7]))
