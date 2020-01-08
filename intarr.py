def interleave(*args):
    output = []
    end = False
    index = 0
    print("start")
    while not end:
        end = True
        for i in args:
            if len(i) > index:
                end = False
                output.append(i[index])
            else:
                output.append(None)
        index += 1
    return output[:-1]

print(interleave([1,2,3,11], [4,5,6,12], [7,8,9,10,15]))
