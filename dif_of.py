def twos_difference(lst):
    lst.sort()
    output = []
    for i in lst:
        if i + 2 in lst:
            output.append((i, i+2))
    return output
