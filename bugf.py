def find_longest(string):
    spl = list(map(str, string.split(" ")))
    print(spl)
    longest = 0
    i=0
    print(len(spl))
    while i < len(spl):
        print(spl[i])
        if len(spl[i]) > longest:
            longest = len(spl[i])
        i += 1
    return longest

print(find_longest("asd asd fasdf asdfas fasdf sadfsadf sd"))
