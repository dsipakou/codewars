def alph(s):

    return ''.join(x for x in sorted(s, key=lambda x: x.lower()) if x.isalpha())

print(alph("ABCccECabc"))
