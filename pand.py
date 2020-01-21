def infected(s):
    s = list(s)
    for i in range(len(s) - 1):
        if s[i] == "1" and s[i + 1] != "X":
            s[i + 1] = "1"
    for i in range(len(s) - 1, 0, -1):
        if s[i] == "1" and s[i - 1] != "X":
            s[i - 1] = "1"
    return s.count("1") * 100 / (s.count("1") + s.count("0"))


print(infected("01000000X000X011X0X"))
