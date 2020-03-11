def rem(arr):
    output = []
    for item in arr:
        if item not in output:
            output.append(item)
    return output

print(rem([
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
    {'data': {'id': 'E'}}]))
