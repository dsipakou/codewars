def freqAlphabets(s: str):
    current_num = ""
    output = []
    left = 0
    while left < len(s):
        if left < len(s) - 2 and '#' in s[left:left+3]:
            print(s[left:left+2])
            output.append(chr(ord('a') + int(s[left:left+2]) - 1))
            left += 3
        else:
            output.append(chr(ord('a') + int(s[left]) - 1))
            left += 1
    return ''.join(str(s) for s in output)

print(freqAlphabets('10#11#12'))
