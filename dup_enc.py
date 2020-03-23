from collections import Counter

def duplicate_encode(word):
    d = Counter(word.lower())
    output = ""
    for c in word:
        if d[c.lower()] == 1:
            output += "("
        else:
            output += ")"
    return output
