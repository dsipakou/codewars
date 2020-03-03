def solution(s):
    output = []
    if len(s) % 2 == 1:
        s += "_"
    for i in range(len(s) // 2):
        output.append(s[i * 2: i * 2 + 2])
    return output
print(solution("asdfasdfa"))
