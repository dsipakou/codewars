def fb():
    for i in range(1, 101):
        line = ""
        if i % 3 == 0:
            line += "Fizz"
        if i % 5 == 0:
            line += "Buzz"
        if line:
            print(line)
        else:
            print(i)

print(fb())
