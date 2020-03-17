def num_sli(n, m):
    if n == m == 0:
        return 0
    return max(n, m) - 1 + ((min(n, m) - 1) * max(n, m))
