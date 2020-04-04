t = int(input())
for tt in range(t):
    n = int(input())
    intervals = sorted(list(map(int, input().split())) for ___ in range(n))
    c = 0
    j = 0
    output = ""
    impossible = False
    for interval in intervals:
        if interval[0] >= c:
            output += "C"
            c = interval[1]
        elif interval[0] >= j:
            output += "J"
            j = interval[1]
        else:
            print("Case #{}: IMPOSSIBLE".format(tt + 1))
            impossible = True
            break
    if not impossible:
        print("Case #{}: {}".format(tt + 1, output))
