def parse(data):
    i = 0
    output = []
    for ch in data:
        if ch == 'i':
            i += 1
        elif ch == 'd':
            i -= 1
        elif ch == 's':
            i = i ** 2
        elif ch == 'o':
            output.append(i)
    return output

print(parse("isoisoiso"))
