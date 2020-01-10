def endless_string(string, start, length):
    calc_start = start % len(string)
    remain = length - (length - calc_start)
    whole = remain // length
    end = remain % length
    print(remain, whole, end)
    return string[calc_start:]

print(endless_string('asdf', 3, 4))



#  65 4321 0123 4567 89
# "as dfas dfas dfas df"
