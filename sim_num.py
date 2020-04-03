def simplify(number): 
    output = ""
    s = str(number)
    for index, ch in enumerate(s[::-1]):
        tmp = ""
        if ch != "0":
            tmp = ch + "*1" if index > 0 else ch
            tmp += "0" * index
            if output != "":
                tmp += "+"
        output = tmp + output
    return output

print(simplify(1234))