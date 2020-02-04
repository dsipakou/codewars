def exc_w(a, b):
    len_b = len(b)
    b.extend(reversed(a))
    print(b, len_b)
    a.clear()
    i = len_b - 1
    while i >= 0:
        a.append(b[i])
        del b[i]
        i -= 1

print(exc_w(['a', 'b', 'c'], [1,2,3]))
