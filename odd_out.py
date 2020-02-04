def odd_out(s):
    output = []
    i = len(s) - 1
    while i >= 0:
        current = s[i]
        if s.count(current) % 2 == 1 and current not in output:
            output.insert(0, current)
        i -= 1
    return output

print(odd_out('aassddffggg'))
