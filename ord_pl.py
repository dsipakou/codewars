def order(sentence):
    d = {}
    for sent in sentence.split():
        for ch in sent:
            if ch.isdigit():
                d[int(ch)] = sent
                break
    output = []
    for i in range(1, 10):
        if i in d:
            output.append(d[i])
    print(' '.join(str(s) for s in output))

order("is2 Thi1s T4est 3a")
