def lottery(s):
    return ''.join(ss for ss in list(filter(str.isdigit, s)))

print(lottery("ffaQtaRFK567eGIIBIcSJtg"))
