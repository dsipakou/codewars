def quickSort(array):
    return main_job(array, 0, len(array)-1)

def main_job(array, start, end):
    print(start, end)
    if start > end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        if array[left] >= array[pivot] and array[right] < array[pivot]:
                array[left], array[right] = array[right], array[left]
        if array[left] < array[pivot]:
                left += 1
        if array[right] >= array[pivot]:
                right -=1
    array[pivot], array[right] = array[right], array[pivot]
    main_job(array, start, right - 1)
    main_job(array, right + 1, end)
    return array

def caesar(string, key):
    output = ""
    for i in string:
        current_chr = (ord(i) - 97 + key) % 26
        output += chr(current_chr + 97)
    return output

def lps(string):
    current_ls = string[0]
    for i in range(1, len(string)):
        left = right = i
        current_ls = max(current_ls, helper(string, left, right), key=lambda x: len(x))
    for i in range(1, len(string)):
        left = i - 1
        right = i
        if string[left] == string[right]:
            current_ls = max(current_ls, helper(string, left, right), key=lambda x: len(x))
    return current_ls

def helper(string, left, right):
    while left > 0 and right < len(string) - 1:
        if string[left - 1] == string[right + 1]:
            left -= 1
            right += 1
        else:
            break
    return string[left:right+1]

def group_an(words):
    sort_words = [''.join(x for x in sorted(y)) for y in words]
    d = {}
    for index, value in enumerate(sort_words):
        print(d)
        d[value] = d.get(value, [])
        d[value].append(index)
    output = []
    for i in d.values():
        tmp = []
        for j in i:
            tmp.append(words[j])
        output.append(tmp)
    return output


print(group_an(["yo", "act", "flop", "tac", "cat", "oy", "olfp"]))
