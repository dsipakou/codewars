t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    if (x & 1 == y & 1):
        print('impossible')