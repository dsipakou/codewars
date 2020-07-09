def longestIncreasingSubsequence(array):
    print(array)
    len_arr = [1 for _ in range(len(array))]
    seq = [None for _ in range(len(array))]
    for i in range(len(array)):
        for j in range(i):
            if array[i] > array[j] and len_arr[j] + 1 > len_arr[i]:
                len_arr[i] = len_arr[j] + 1
                seq[i] = j
    cur_max = -1
    idx = -1
    for i in range(len(array)):
        if len_arr[i] > cur_max:
            cur_max = len_arr[i]
            idx = i
    output = []
    print(len_arr)
    print(seq, idx)
    while idx is not None:
        output.append(array[idx])
        idx = seq[idx]
    print(output)
    return output[::-1] if len(output) > 0 else [-1]
