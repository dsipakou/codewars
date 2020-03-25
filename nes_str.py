def same_structure_as(original,other):
    print(original, other)
    brackets = ("[", "]")
    or_stack = ""
    ot_stack = ""
    open = False
    for c in str(original):
        if c == '\'':
            open = not open
        elif c in brackets and not open:
            or_stack += c
        else:
            or_stack += "_"
    for c in str(other):
        if c == '\'':
            open = not open
        elif c in brackets and not open:
            ot_stack += c
        else:
            ot_stack += "_"
    return or_stack == ot_stack
