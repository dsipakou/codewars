def end_w(string, ending):
    return string[-len(ending):] == ending

print(end_w('abcde', 'dee'))
