def endless_string(string, start, length):
    calc_start = start % len(string)
    return string[start:]

print(endless_string('asdf', -3, 4))



#  65 4321 0123 4567 89
# "as dfas dfas dfas df"
