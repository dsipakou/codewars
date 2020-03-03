def ind_eq_val(arr):
    left = 0
    right = len(arr) - 1
    output = []
    while left <= right:
        index = (right + left) // 2
        if arr[index] == index:
            output.append(index)
            right = index - 1
        if arr[index] < index:
            left = index + 1
        else:
            right = index - 1
    return min(output) if len(output) > 0 else -1

print(ind_eq_val([-1, 0, 1, 2]))
