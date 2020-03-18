def josephus_survivor(n,k):
    print(n, k)
    arr = list(range(1, n+1))
    index = 0
    while len(arr) > 1:
        index = (index + k - 1) % len(arr)
        arr.pop(index)
    return arr[0]
