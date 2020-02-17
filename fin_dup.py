def dcount(text):
    d = {}
    output = 0
    for c in text:
        d[c] = d.get(c, 0)
        d[c] += 1
        if d[c] == 2:
            output += 1
    return output

print(dcount("abcdea"))
