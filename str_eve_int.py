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
    start = list(bin(n)[2:] + '1'*(len(bin(m)[2:]) - len(bin(n)[2:])))
    output = start[:]
    for i in range(len(start) - 1, 0, -1):
        if start[i] != '0':
            start[i] = '0'
            start[i - 1] = '1'
        current_int = int(''.join(s for s in start), base=2)
        if current_int >= n and current_int <= m:
            output = start[:]
    return int(''.join(s for s in output), base=2)

def strongest_even(n, m):
    while True:
        if m & m - 1 < n: return m
        m &= m - 1

print(str_even(129, 193))
