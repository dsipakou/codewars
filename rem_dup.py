def remove_dup(s):
    s = list(map(str, s.split()))
    output = []
    s1 = set(s)
    for i in s:
        if i in s1:
            output.append(i)
            s1.discard(i)
    return ' '.join(ss for ss in output)

print(remove_dup("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"))
