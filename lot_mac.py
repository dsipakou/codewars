def lottery(s):
    output = ""
    for i in range(len(s)):
        if s[i].isdigit() and s[i] not in output:
            output += s[i]
    return output or 'One more run!'

print(lottery("ffaQtaRFKeGIIBIcSJtg"))
