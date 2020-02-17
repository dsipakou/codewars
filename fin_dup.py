def dcount(text):
    d = {}
    output = 0
    for c in text:
        d[c.lower()] = d.get(c.lower(), 0)
        d[c.lower()] += 1
        if d[c.lower()] == 2:
            output += 1
    return output

print(dcount("abcdea"))
