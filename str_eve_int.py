from datetime import datetime

def strongest_even(n, m):
    start_time = datetime.now()
    start = n
    strongest = n
    max_even = 0
    start_time = datetime.now()
    for i in range(start, m + 1):
        a = i
        index = list(str(bin(i)))[::-1].index('1')
        print(i, index, bin(i))
        if index > max_even:
            strongest = i
            max_even = index
#    print(datetime.now() - start_time)
    return strongest

def str_even(n, m):
    start_time = datetime.now()
    start = '1'
    while int(start, base=2) <= m:
        start += '0'
    start = start[:-1]
    index = 1
    while int(start, base=2) > m or int(start, base=2) < n:
        index += 1
        start = '1' * index + start[index:]
    print(datetime.now() - start_time)
    return int(start, base=2)

print(str_even(1408026681, 1589848532))
