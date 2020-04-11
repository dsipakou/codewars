def sort_number(a): 
    a.sort()
    a[-1] = 1 if a [-1] != 1 else 2
    return sorted(a)