def same_structure_as(original,other):
    brackets = ("[", "]")
    or_stack = []
    ot_stack = []
    for c in str(original):
        if c in brackets:
            or_stack.append(c)
        else:
            or_stack.append("_")
    for c in str(other):
        if c in brackets:
            ot_stack.append(c)
        else:
            ot_stack.append("_")
    print(or_stack, ot_stack)
    return or_stack == ot_stack
