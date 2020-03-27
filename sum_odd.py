def row_sum_odd_numbers(n):
    start_num = n ** 2 - n + 1
    return sum(start_num + i * 2 for i in range(n))
