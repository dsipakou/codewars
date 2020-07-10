def squareOfZeroes(matrix):
    dp = [[None] * len(matrix[0]) for _ in range(len(matrix))]
    for i in reversed(range(len(matrix))):
        for j in reversed(range(len(matrix[0]))):
            right = bottom = 0
            if j == len(matrix[0]) - 1:
                if matrix[i][j] == 0:
                    right = 1
            elif matrix[i][j] == 0:
                right = dp[i][j + 1][0] + 1
            if i == len(matrix) - 1:
                if matrix[i][j] == 0:
                    bottom = 1
            elif matrix[i][j] == 0:
                bottom = dp[i + 1][j][1] + 1
            dp[i][j] = [right, bottom]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            sq_len = 2
            while sq_len <= len(matrix) - j and sq_len <= len(matrix) - i:
                i2 = i + sq_len - 1
                j2 = j + sq_len - 1
                if is_square(dp, i, j, i2, j2):
                    return True
                sq_len += 1
    return False

def is_square(db, i, j, i2, j2):
    print(i, j, i2, j2, db[i][j], db[i2][j], db[i][j2])
    sq_len = j2 - j + 1
    is_top = db[i][j][1] >= sq_len
    is_left = db[i][j][0] >= sq_len
    is_bottom = db[i2][j][0] >= sq_len
    is_right = db[i][j2][1] >= sq_len
    return is_top and is_left and is_bottom and is_right
