def get_free_urinals(urinals):
    free = True
    output = 0
    i = 0
    while i < len(urinals) - 1:
        if urinals[i] == "1":
            free = False
            if urinals[i + 1] == "1":
                return -1
        else:
            if free == True and urinals[i + 1] == "0":
                output += 1
                free = False
            else:
                free = True
        i += 1
    return output + 1 if free and urinals[i] == "0" else output

print(get_free_urinals("00000"))
