def ver_ev(n):
    output = str(n)
    while len(output) > 1:
        output = str(sum([int(x) for x in output]))
    return int(output) % 2 == 0

print(ver_ev(177))
