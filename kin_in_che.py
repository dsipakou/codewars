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
                empty = True
                if king[0] == fig_item[1][0]:
                    print("Vertical")
                    start = min(king[1], fig_item[1][1]) + 1
                    end = max(king[1], fig_item[1][1])
                    for i in range(start, end):
                        print(chessboard[king[0]][i])
                        if chessboard[king[0]][i] != ' ':
                            empty = False
                            break
                else:
                    print("Horizont")
                    start = min(king[0], fig_item[1][0]) + 1
                    end = max(king[0], fig_item[1][0])
                    print(king, fig_item, start, end)
                    for i in range(start, end):
                        print(i, king[1])
                        print(chessboard[i][king[1]])
                        if chessboard[i][king[1]] != ' ':
                            empty = False
                            break
                if empty:
                    return True
        if fig_item[0] == '♟':
            if (king[0] - fig_item[1][0]) == 1 and abs(king[1] - fig_item[1][1]) == 1:
                return True
        if fig_item[0] == '♞':
            print(king, fig_item)
            left = abs(king[0] - fig_item[1][0])
            right = abs(king[1] - fig_item[1][1])
            print(left, right)
            if (left == 1 and right == 2) or (left == 2 and right == 1):
                return True
    return False


print(king([
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ','♜',' ',' '],
            [' ','♜',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ','♞',' ',' ',' ',' ',' '],
            ['♔',' ',' ',' ',' ',' ',' ',' ']
        ]))
