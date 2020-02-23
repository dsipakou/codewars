def end_w(string, ending):
    return len(ending) == 0 or string[-len(ending):] == ending

print(end_w('abcde', ''))
