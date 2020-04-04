t = int(input())
for tt in range(t):
    n = int(input())
    rows = cols = 0
    matrix = [list(map(int, input().split())) for _ in range(n)]
    rot_matrix = [[matrix[i][j] for i in range(n)] for j in range(n)]
    summ = sum(matrix[i][i] for i in range(n))
    for i in range(n):
        if len(set(matrix[i])) < n:
            rows += 1
        if len(set(rot_matrix[i])) < n:
            cols += 1
    print("Case #{}: {} {} {}".format(tt + 1, summ, rows, cols))