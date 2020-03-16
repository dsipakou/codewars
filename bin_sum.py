def addbin(a, b):
    return bin(int(a, base=2) + int(b, base=2))[2:]

print(addbin("11", "1"))
