def solve():
    return fib()

def fib():
    seq = [1, 2]
    output = 2
    while seq[1] < 4000000:
        print(seq, output)
        seq[0], seq[1] = seq[1], seq[0] + seq[1]
        if seq[1] % 2 == 0:
            output += seq[1]
    return output

print(solve())