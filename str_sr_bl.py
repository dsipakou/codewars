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
    for a in sorted("21AxBz", key=lambda x: x.isupper()):
        print(a)
    for output_item in output:
        output_str += ''.join(str(item) for item in output_item)
        output_str += '-'
    print(output_str[:-1])

blocks("21AxBzFCA")
