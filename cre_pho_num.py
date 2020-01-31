def create_num(n):
    output = "({}) {}-{}".format(''.join(str(s) for s in n[:3]), ''.join(str(s) for s in n[3:6]), ''.join(str(s) for s in n[6:]))
    return output

print(create_num([1,2,3,4,5,6,7,8,9,0]))
