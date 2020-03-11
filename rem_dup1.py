def rem(arr):
    output = []
    for item in arr:
        if item not in output:
            output.append(item)

    output1 = [eval(d1) for d1 in set(sorted(str(d) for d in arr))]
    return output1

print(rem(
[
    {'data': {'id': 'A'}},
    {'data': {'id': 'A'}},
    {'data': {'id': 'A'}},
    {'data': {'id': 'A'}},
    {'data': {'id': 'B'}},
    {'data': {'id': 'B'}},
    {'data': {'id': 'D'}},
    {'data': {'id': 'D'}},
    {'data': {'id': 'B'}},
    {'data': {'id': 'B'}},
    {'data': {'id': 'B'}},
    {'data': {'id': 'B'}},
    {'data': {'id': 'E'}},
    {'data': {'id': 'E'}}
]))
