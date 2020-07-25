import sys
print(sys.getrecursionlimit())

def solve(a,b):
    if a == 0 or b == 0:
        return [a, b]
    if a >= 2*b:
        return solve(a - 2*b, b)
    if b >= 2 * a:
        return solve(a, b - 2*a)
    return [a, b]
    
