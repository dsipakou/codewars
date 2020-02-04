def exc_w(a, b):
    len_a = len(a)
    b.extend(reversed(a))
    a.clear()
    i = len_a - 1
    while i >= 0:
        a.append(b[i])
        i -= 1
    b = b[len_a:]
    return a, b

print(exc_w(['a', 'b', 'c'], [1,2,3]))
