def rgb(r, g, b):
    r = min(max(r, 0), 255)
    g = min(max(g, 0), 255)
    b = min(max(b, 0), 255)
    r = hex(r)[2:].upper().rjust(2, '0')
    g = hex(g)[2:].upper().rjust(2, '0')
    b = hex(b)[2:].upper().rjust(2, '0')
    
    return r+g+b