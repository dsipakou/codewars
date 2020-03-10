def yes_no(arr):
    output = [False for _ in range(len(arr))]
    output1 = []
    take = True
    while False in output:
        i = 0
        while i < len(arr):
            if take and not output[i]:
                take = False
                output[i] = True
                output1.append(arr[i])
            elif not output[i]:
                take = True
            i += 1
    return output1




print(yes_no(['this', 'code', 'is', 'right', 'the']))
