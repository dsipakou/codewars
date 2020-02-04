def odd_out(s):
    d = {}
    for i in s:
        if i in d:
            del d[i]
        else:
            d[i] = None
    return list(d.keys())

print(odd_out('Whats going on'))
