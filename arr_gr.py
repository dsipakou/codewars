def gs(word, possible_words):
    w = sorted(word)
    output = []
    for i in possible_words:
        if sorted(i) == w:
            output.append(i)

    return output

print(gs("ortsp", ["sport", "parrot", "ports", "matey"]))
