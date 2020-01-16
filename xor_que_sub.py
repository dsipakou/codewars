def xor_here(arr, queries):
    output = []
    for i in queries:
        tmp = 0
        for j in range(i[0], i[1] + 1):
            tmp ^= arr[j]
        output.append(tmp)
    return output

print(xor_here([4,8,2,10], [[2,3], [1,3], [0,0], [0,3]]))
