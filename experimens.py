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
import re

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

# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    arr = []
    helper(0, arr, root)


def helper(sum, arr, node):
    if node is None:
            return

    current_sum = sum + node.value

    if node.left is None and node.right is None:
        arr.append(current_sum)
        return

    helper(current_sum, arr, node.left)
    helper(current_sum, arr, node.right)

from datetime import datetime
from datetime import timedelta

def calendar_1(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    calendar1.insert(0, ['0:00', dailyBounds1[0]])
    calendar1.append([dailyBounds1[1], '23:59'])
    calendar2.insert(0, ['0:00', dailyBounds2[0]])
    calendar2.append([dailyBounds2[1], '23:59'])
    left1 = left2 = 1
    merged_calendar = [calendar1[0], calendar2[0]]
    while left1 < len(calendar1) and left2 < len(calendar2):
        date1_start = datetime.strptime(calendar1[left1][0], '%H:%M')
        date2_start = datetime.strptime(calendar2[left2][0], '%H:%M')
        if left2 >= len(calendar2) or date1_start < date2_start:
            merged_calendar.append(calendar1[left1])
            left1 += 1
        else:
            merged_calendar.append(calendar2[left2])
            left2 += 1
    output = []
    cur_max_end = None
    verbal_cur_max_end = None
    for i in range(len(merged_calendar) - 1):
        cur_end = datetime.strptime(merged_calendar[i][1], '%H:%M')
        if cur_max_end is None:
            cur_max_end = cur_end
            verbal_cur_max_end = merged_calendar[i][1]
        if cur_end > cur_max_end:
            cur_max_end = cur_end
            verbal_cur_max_end = merged_calendar[i][1]
        cur_max_end = max(cur_max_end, cur_end)
        next_start = datetime.strptime(merged_calendar[i + 1][0], '%H:%M')
        delta_time = timedelta(minutes=meetingDuration)
        if next_start - cur_max_end >= delta_time:
            output.append([verbal_cur_max_end, merged_calendar[i + 1][0]])
    print(merged_calendar)
    return output

calendar1 = [['9:00', '10:30'], ['11:30', '13:00'], ['14:00', '16:00'], ['16:00', '18:00']]
calendar2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
dailyBounds1 = ['8:00', '18:00']
dailyBounds2 = ['7:00', '18:30']
meetingDuration = 45




def moveEl(array, toMove):
    right = len(array) - 1
    left = 0
    while left < right:
        if array[left] == toMove:
            if array[right] != toMove:
                array[right], array[left] = array[left], array[right]
                left += 1
            right -= 1
        else:
            left += 1
    return array

def balancedBrackets(string):
    close_brackets = ']})'
    mapping = {'}': '{', ']': '[', ')': '('}
    stack = []
    for s in string:
        if s in close_brackets:
            if not len(stack) or not stack.pop() == mapping[s]:
                return False
            else:
                stack.append(s)
    return len(stack) == 0


def zigzagTraverse(array):
    direction = "down"
    size = {'row': len(array) - 1, 'col': len(array[0]) - 1}
    col = row = 0
    output = []
    while col <= size['col'] and row <= size['row']:
        output.append(array[row][col])
        if direction == "down":
            if col == 0 or row == size['row']:
                if row == size['row']:
                    col += 1
                else:
                    row += 1
                direction = "up"
            else:
                row += 1
                col -= 1
        else:
            if row == 0 or col == size['col']:
                if col == size['col']:
                    row += 1
                else:
                    col += 1
                direction = "down"
            else:
                row -= 1
                col += 1
    return output

def knuth_morris_pratt(string, substring):
    template = [-1]
    left = 0
    right = 1
    while right < len(substring):
        if substring[left] == substring[right]:
            template.append(left)
            left += 1
            right += 1
        else:
            if left > 0:
                left = template[left - 1] + 1
            else:
                template.append(-1)
                right += 1
    up = 0
    down = 0
    while down < len(substring) and up < len(string):
        if down < 0:
            down = 0

        if string[up] == substring[down]:
            up += 1
            down += 1
        else:
            if down > 0:
                down = template[down - 1] + 1
            else:
                up += 1
    return True if down >= len(substring) else False


rrr = re.compile(r'ALTER TABLE\s+\"?\'?\w+\"?\'?\s+DROP COLUMN', re.IGNORECASE | re.MULTILINE)
rrr1 = re.compile(r'ALTER TABLE')

def underscore(string, substring):
    arr = get_arr(string, substring)
    arr = merge_arr(arr)
    output = form_string(string, arr)
    return output

def get_arr(string, substring):
    i = 0
    arr = []
    while i < len(string):
        idx = string[i:].find(substring, i)
        if idx >= 0:
            arr.append([idx, idx + len(substring)])
            i = idx + 1
        else:
            break
    return arr

def merge_arr(arr):
    output = []
    if len(arr) == 0:
        return output
    left = arr[0][0]
    right = arr[0][1]
    for i in range(len(arr)):
        if arr[i][0] <= right:
            right = arr[i][1]
        else:
            output.append([left, right])
            left = arr[i][0]
            right = arr[i][1]
    output.append([left, right])
    return output

def form_string(string, arr):
    if len(arr) == 0:
        return string
    left = 0
    right = 0

    output = ""
    for i in range(len(arr)):
        tmp_left = arr[i][0]
        tmp_right = arr[i][1]
        output += ''.join(s for s in string[left:tmp_left])
        output += "_"
        output += ''.join(s for s in string[tmp_left:tmp_right])
        output += "_"
        left = arr[i][1]
    output += string[left:]
    return output

from urllib.parse import urlencode

def k_profit():
    pass

def quickselect(array, k):
    return helper(array, k - 1, 0, len(array) - 1)

def helper(array, k, start, end):
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        if array[left] > array[pivot] and array[right] < array[pivot]:
            array[left], array[right] = array[right], array[left]
        if array[left] <= array[pivot]:
            left += 1
        if array[right] >= array[pivot]:
            right -= 1
    array[pivot], array[right] = array[right], array[pivot]
    if right == k:
        return array[right]
    elif right > k:
        return helper(array, k, start, right - 1)
    else:
        return helper(array, k, right + 1, end)

print(quickselect([8,5,2,9,7,6,3], 3))
