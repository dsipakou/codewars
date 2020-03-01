import sys
sys.setrecursionlimit(10**6)

def per_rec(n):
    d = {
        0: 0,
        1: 1,
        2: 1,
    }
    helper(n, d)
    return sum(d.values()) * 4

def helper(n, d):
    if n not in d:
        d[n] = helper(n - 1, d) + helper(n - 2, d)
    return d[n]

print(per_rec(41988))
