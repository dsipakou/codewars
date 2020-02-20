def pol(x):
    for i in range(1, len(str(x)) + 1):
        if int(str(x)[:i]) % i != 0:
            return False
    return True

print(pol(1234))
