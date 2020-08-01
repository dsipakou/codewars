def solve(s):
    l = 0
    r = len(s) - 1
    output = list(s)
    while l < r:
        if output[l] == ' ' or output[r] == ' ':
            if output[l] == ' ':
                l += 1
            if output[r] == ' ':
                r -= 1
        else:
            output[l], output[r] = output[r], output[l]
            l += 1
            r -= 1
    return (''.join(ss for ss in output))
        
