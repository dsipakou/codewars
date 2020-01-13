def min_num_taxis(requests):
    left = min([x for x, y in requests])
    right = max([y for x, y in requests])
    output = [0 for x in range(left, right + 1)]
    for i in requests:
        for j in range(i[0], i[1]):
            output[j - left] += 1
    return max(output)

print(min_num_taxis([(1,4), (2,5), (1, 10), (4,5)]))
