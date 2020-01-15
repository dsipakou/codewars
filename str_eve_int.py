from datetime import datetime

def strongest_even(n, m):
    mem = {}
    start = n
    strongest = n
    max_even = 0
    start_time = datetime.now()
    if n % 2 == 1:
        start = n + 1
    for i in range(start, m + 1, 2):
        a = i
        index = helper(mem, i)
        if index > max_even:
            strongest = i
            max_even = index
    return strongest

def helper(mem, n):
    if n in mem:
        return mem[n]
    if n % 2 == 1:
        return 0
    mem[n] = 1 + helper(mem, n / 2)
    return mem[n]

print(strongest_even(10,5880000))
