def solve():
    output = 0
    for i in range(1000):
        if i % 5 == 0 or i % 3 == 0:
            output += i
    print(output)

solve()
