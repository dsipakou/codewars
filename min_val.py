def minval(arr):
    arr = sorted(set(arr))
    return int(''.join(str(i) for i in arr))


print(minval([1,3,1]))
