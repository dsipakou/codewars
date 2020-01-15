def strongest_even(n, m):
    start = n
    if n % 2 == 1:
        start = n + 1
    for i in range(n, m + 1):
        a = i
        index = 0
        while a % 2 == 0:
            index += 1
            a /= 2
        print("Number is: ", i, " and strongest even is: ", index)

print(strongest_even(10,28))
