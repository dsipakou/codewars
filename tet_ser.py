def get_score(arr):
    levels = [40, 100, 300, 1200]
    current_level = 0
    output = 0
    lines = 0
    for i, v in enumerate(arr):
        if v > 0:
            print("Element: ", i, " output: ", output, " value: ", v, "level :", current_level, "lines: ", lines)
            output += levels[v - 1] * (current_level + 1)
            lines += v
            if lines >= 10:
                current_level += 1
                lines -= 10

    return output

print(get_score([2, 2, 4, 4, 4, 2, 1, 4, 1, 2, 4, 3]))
