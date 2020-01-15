from datetime import datetime

def strongest_even(n, m):
    start_time = datetime.now()
    mem = {}
    start = n
    strongest = n
    max_even = 0
    start_time = datetime.now()
    if n % 2 == 1:
        start = n + 1
    for i in range(start, m + 1):
        a = i
        index = list(str(bin(i)))[::-1].index('1')
        if index > max_even:
            strongest = i
            max_even = index
    print(datetime.now() - start_time)
    return strongest

print(strongest_even(10,12000000))
