from itertools import chain

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
    return output[:-len(args)]

print(interleave([1,2,3,11], [4,5,6,12], [7,8,9,10,15]))


# from itertools import chain, zip_longest

# def interleave(*args):
#     return list(chain.from_iterable(zip_longest(*args)))
