def min_fli(a, b, c):
    bin_a = format(a, '020b')
    bin_b = format(b, '020b')
    bin_c = format(c, '020b')
    output = 0
    for i in range(len(bin_a) - 1, -1, -1):
        if bin_c[i] == '1':
            if bin_a[i] == '0' and bin_b[i] == '0':
                output += 1
        else:
            if bin_a[i] == '1':
                output += 1
            if bin_b[i] == '1':
                output += 1
    return output


print(min_fli(82801542,6,5))
