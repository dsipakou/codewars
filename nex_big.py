def next_bigger(n):
    if n < 10:
        return -1
    num = list(str(n))
    for i in range(len(num) - 1, 0, -1):
        if int(num[i]) > int(num[i-1]):
            tmp = num[i:]
            tmp.sort()
            for j in range(len(tmp)):
                if tmp[j] > num[i - 1]:
                    tmp[j], num[i-1] = num[i-1], tmp[j]
                    break
            num[i:] = tmp
            return int(''.join(nn for nn in num))
    return -1