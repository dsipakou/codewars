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
    output = {}
    for w in words:
        sort_word = ''.join(sorted(w))
        if sort_word in output:
            output[sort_word].append(w)
        else:
            output[sort_word] = [w]
    return list(output.values())



class TempClass:
    def __init__(self, title):
        self._title = title

    def __repr__(self):
        return self._title

    def __doc__(self):
        return "Here is doc: " + self._title

def long_sub(string):
    d = {}
    start = 0
    output = [0, 1]
    for i in range(len(string)):
        if string[i] in d:
            start = max(start, d[string[i]] + 1)
        d[string[i]] = i
        if output[1] - output[0] < i + 1 - start:
            output = [start, i + 1]
    return string[output[0]:output[1]]

from decimal import *
from functools import wraps
from time import perf_counter

def timeit_wrapper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        func_return_val = func(*args, **kwargs)
        end = perf_counter()
        print('{0:<10}.{1:<8} : {2:<8}'.format(func.__module__, func.__name__, end - start))
        return func_return_val
    return wrapper

@timeit_wrapper
def exp(x):
    getcontext().prec += 2
    i, lasts, s, fact, num = 0, 0, 1, 1, 1
    while s != lasts:
        lasts = s
        i += 1
        fact *= i
        num *= x
        s += num / fact
    getcontext().prec -= 2
    return +s

print(exp(Decimal(400)))
