def calculate(s):
    s = s.replace("plus", "+").replace("minus", "-")
    return eval(s)

print(calculate("896minus738"))
