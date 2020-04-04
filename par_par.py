t = int(input())
for tt in range(t):
    n = int(input())
    intervals = sorted([list(map(int, input().split())), i] for i in range(n))
    c = 0
    j = 0
    output = []
    impossible = False
    for interval in intervals:
        if interval[0][0] >= c:
            output.append([interval[1], "C"])
            c = interval[0][1]
        elif interval[0][0] >= j:
            output.append([interval[1], "J"])
            j = interval[0][1]
        else:
            print("Case #{}: IMPOSSIBLE".format(tt + 1))
            impossible = True
            break
    if not impossible:
        print("Case #{}: {}".format(tt + 1, ''.join(str(a[1]) for a in sorted(output))))
