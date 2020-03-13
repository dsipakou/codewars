def occ(order, max_e):
    output = []
    d = {}
    for i in order:
        d[i] = d.get(i, 0)
        d[i] += 1
        if d[i] <= max_e:
            output.append(i)
    return(output)

print(occ([1,1,3,3,7,2,2,2,2], 3))
