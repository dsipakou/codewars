def blocks(s):
    output = []
    for c in s:
        added = False
        for i, v in enumerate(output):
            if c not in output[i]:
                added = True
                output[i].append(c)
                break
        if not added:
            output.append([c])
    output_str = ''
    print(sorted(s, key=lambda x: (x.isdigit(), x.isupper(), x)))

blocks("21AxBzFCA")
