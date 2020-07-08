def longestStringChain(strings):
    d = {}
    cur_max = 0
    cur_max_word = ''
    strings.sort(key=lambda x: len(x), reverse=False)
    for word in strings:
        if len(word) > 1:
            found = False
            for i in range(len(word)):
                cur_word = word[:i] + word[i + 1:]
                if cur_word in d:
                    if word in d:
                        if d[cur_word]['chain'] + 1 > d[word]['chain']:
                            d[word] = {'prev': cur_word, 'chain': d[cur_word]['chain'] + 1}
                    else:
                        d[word] = {'prev': cur_word, 'chain': d[cur_word]['chain'] + 1}
                    found = True
            if not found:
                d[word] = {'prev': '', 'chain': 1}
        else:
            d[word] = {'prev': '', 'chain': 1}
        if d[word]['chain'] > cur_max:
            cur_max_word = word
            cur_max = d[word]['chain']
    
    output = []
    while True:
        output.append(cur_max_word)
        print(cur_max_word, d)
        if d[cur_max_word]['prev'] in d:
            cur_max_word = d[cur_max_word]['prev']
        else:
            break

    return output if cur_max > 1 else []
            
