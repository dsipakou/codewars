def test(lines):
    d = []
    for i, v in enumerate(lines):
        d.append(f'{i + 1}: {v}')
    return d

print(test(["a", "b", "c"]))
