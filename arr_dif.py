def array_diff(a, b):
    d = {i: True for i in b}
    output = []
    for i in a:
        if d.get(i):
            continue
        else:
            output.append(i)
    return output

print(array_diff([1,2,2], [2]))
