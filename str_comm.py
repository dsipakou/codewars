def sol(string, markers):
    output = ''
    current_string = ''
    comment = False
    for ch in string:
        if ch == '\n':
            current_string = current_string.strip()
            comment = False
        if not comment:
            if ch in markers:
                comment = True
            else:
                current_string += ch
                if ch == '\n':
                    output += current_string
                    current_string = ''
    output += current_string.strip()
    return output

print(sol("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
