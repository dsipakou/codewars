def array_diff(a, b):
    output = []
    left = 0
    left1 = 0
    while left < len(a) and left1 < len(b):
        current = 0
        if b[left1] == a[left]:
            left += 1
        elif b[left1] < a[left]:
            left1 += 1
        elif current != a[left]:
            output.append(a[left])
            current = a[left]
            left += 1

    output.extend(a[left:])
    return output


print(array_diff([1,2,2], [2]))
