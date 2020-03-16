def set_mat(matrix):
    coord = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                coord.append((i, j))
    for co in coord:
        set_row_zeroes(matrix, co[0])
        set_col_zeroes(matrix, co[1])
    return matrix

def set_row_zeroes(matrix, index):
    for i in range(len(matrix[0])):
        matrix[index][i] = 0

def set_col_zeroes(matrix, index):
    for i in range(len(matrix)):
        matrix[i][index] = 0

print(set_mat([[1,1,1], [1,0,1], [1,1,1]]))
