def century(year):
    output = year // 100
    output = output + 1 if year % 10 > 0 else output
    return output

print(century(1900))
