def no_od(values):
    output = []
    for val in values:
        if val % 2 == 0:
            output.append(val)
    return output

print(no_od([1,2,3,4,5]))
