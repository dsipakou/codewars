def fake_bin(x):
    output = []
    for i in x:
        if int(i) < 5:
            output.append(0)
        else:
            output.append(1)
    return ''.join(str(s) for s in output)
