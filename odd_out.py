def odd_out(s):
    output = []
    i = len(s) - 1
    while i >= 0:
        current = s[i]
        if s.count(current) % 2 == 1 and current not in output:
            output.append(current)
        i -= 1
    return output[::-1]

print(odd_out('Whats going on'))
