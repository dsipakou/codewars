def patternMatcher(pattern, string):
    pattern = list(pattern)
    if pattern[0] == 'x':
        letters = {0: 'x', 1: 'y'}
    else:
        letters = {0: 'y', 1: 'x'}
    d_count = {'x': pattern.count('x'), 'y': pattern.count('y')}
    i_len = 1
    while i_len < len(string) - d_count[letters[1]]:
        second_index = pattern.index(letters[1]) * i_len
        first_word = string[0:i_len]
        whole_sec_len = (len(string) - i_len * d_count[letters[0]])
        if whole_sec_len % d_count[letters[1]] == 1:
            i_len += 1
            continue
        second_word = string[second_index:second_index + whole_sec_len // d_count[letters[1]]]
        output = ''
        for ch in pattern:
            if ch == letters[0]:
                output += first_word
            else:
                output += second_word
        if output == string:
            return True
        i_len += 1
    return False

print(patternMatcher('yxyyyxxy', 'baddaddoombaddaddoomibaddaddoombaddaddoombaddaddoombaddaddoomibaddaddoomibaddaddoom'))