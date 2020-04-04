t = int(input())
for _ in range(t):
    s = input()
    output = ""
    current = 0
    for ch in s:
        cur_num = int(ch)
        if cur_num == current:
            output += ch
        elif cur_num > current:
            n = cur_num - current
            output += "("*n + ch
            current = cur_num
        else:
            n = current - cur_num
            output += ")" * n + ch
            current = cur_num
    output += ")"*int(s[len(s) - 1])
    print(output)