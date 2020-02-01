def dig(s):
    output = 0
    for ss in s:
        if ss.isdigit() or (ord(ss) > 64 and ord(ss) < 91) or (ord(ss) > 97 and ord(ss) < 123):
            output += 1
    return output

print(dig("123!@#asd"))
