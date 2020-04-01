def cyc_num(n):
    tmp = bin(n)[2:]
    pivot = len(tmp) % 2
    if pivot % 2 == 0:
        return False
    if tmp.count('0') > 1:
        return False
    if tmp[pivot] != '0':
        return False
    return True
    

print(cyc_num(5))