def yes_no(arr):
    output = [False for _ in range(len(arr))]
    output1 = []
    while False in output:
        i = 0
        take = True
        while i < len(arr):
            if take and not output[i]:
                take = False
                output[i] = True
                output1.append(arr[i])
            elif not output[i]:
                take = True
            i += 1
    return output1




print(yes_no([1,2,3,4,5,6,7]))
