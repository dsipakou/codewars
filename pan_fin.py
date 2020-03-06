def isp(s):
    output = set()
    s = s.lower()
    for c in s:
        current_ch = ord(c)
        if current_ch >= ord('a') and current_ch <= ord('z'):
            output.add(ord(c))
    return len(output) == 26

print(isp("The quick, brown fox jumps over the lazy dog!"))
