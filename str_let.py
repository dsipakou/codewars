from collections import defaultdict

def string_letter_count(s):
    d = defaultdict(int)
    for ch in s:
        if ch.lower() >= 'a' and ch <= 'z':
            d[ch.lower()] += 1
    tp = []
    for k, v in d.items():
        tp.append((v, k))
    tp.sort(key=lambda x: x[1])
    return ''.join(str(s) + str(v) for s, v in tp)