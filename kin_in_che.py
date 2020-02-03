def king(chessboard):
    figures = '♛♝♞♜♟'
    fig_king = '♔'
    fig = []
    king = None
    for i in range(len(chessboard)):
        for j in range(len(chessboard[0])):
            if chessboard[i][j] in figures:
                fig.append([chessboard[i][j], [i, j]])
            elif chessboard[i][j] == fig_king:
                king = [i, j]
    if not len(fig):
        return False
    for fig_item in fig:
        if fig_item[0] == '♝' or fig_item[0] == '♛':
            if abs(king[0] - fig_item[1][0]) == abs(king[1] - fig_item[1][1]):
                return True
        if fig_item[0] == '♜' or fig_item[0] == '♛':
            if (king[0] - fig_item[1][0]) == 0 or (king[1] - fig_item[1][1]) == 0:
                return True
        if fig_item[0] == '♟':
            if (king[0] - fig_item[1][0]) == 1 and abs(king[1] - fig_item[1][1]) == 1:
                return True
        if fig_item[0] == '♞':
            if (abs(king[0] - fig_item[1][0]) == 1 and abs(king[1] - fig_item[1][1] == 2)) or (abs(king[0] - fig_item[1][0]) == 2 and abs(king[1] - fig_item[1][1]) == 1):
                return True
    return False


print(king([
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ','♟',' ',' ',' ',' '],
            [' ',' ','♔',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ']
        ]))
