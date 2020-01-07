def calculate(s):
    left = 0
    right = 0
    left_num = 0
    right_num = 0
    while right <= len(s):
        if s[right].isdigit():
            right += 1
        else:
            tmp_num = int(s[left:right])
            if s[right] == "m"

print(calculate("896minus738"))
