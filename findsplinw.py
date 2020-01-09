def advice(agents, n):
    playground = [[float('inf') for x in range(n)] for y in range(n)]
    for i in agents:
        for j in range(n):
            for k in range(n):
                playground[j][k] = min(playground[j][k], abs(j - i[0]) + abs(k - i[1]))

    current_max = 1
    output_cells = []
    for i in range(n):
        for j in range(n):
            if playground[i][j] > current_max:
                output_cells = [(i, j)]
                current_max = playground[i][j]
            elif playground[i][j] == current_max:
                output_cells.append((i, j))

    return output_cells

print(advice([(0,0), (1, 5), (5, 1)], 6))
