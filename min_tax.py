def min_num_taxis(requests):
    d = {}
    for i in requests:
        for j in range(i[0], i[1]):
            d[j] = d.get(j, 0) + 1
    current_max = 0
    for v in d.values():
        current_max = max(current_max, v)
    return current_max

print(min_num_taxis([(1,4), (2,5), (1, 10), (4,5)]))
