def interweavingStrings(one, two, three):
    print(one, two, three)
    if len(one) + len(two) != len(three):
        return False
    if len(one) == len(two) == len(three) == 0:
        return True

    cur_num = three[0]
    if cur_num in one:
        idx = one.index(cur_num)
        return interweavingStrings(one[:idx] + one[idx + 1:], two, three[1:])
    elif cur_num in two:
        idx = two.index(cur_num)
        return interweavingStrings(one, two[:idx] + two[idx + 1:], three[1:])
    else:
        return False


print(interweavingStrings("aaaaaaa", "aaabaaa", "aaaaaacbaaaaaa"))


