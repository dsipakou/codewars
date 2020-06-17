class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if len(board) < 2:
            return board
        track = [[None] * len(board[0]) for _ in range(len(board))]
        output = 0
        for j in range(len(board[0])):
            if board[0][j] == 'O' and track[0][j] is None:
                self.dfs(board, track, 0, j)
            if board[len(board) - 1][j] == 'O' and track[len(board) - 1][j] is None:
                self.dfs(board, track, len(board) - 1, j)
        for i in range(len(board)):
            if board[i][0] == 'O' and track[i][0] is None:
                self.dfs(board, track, i, 0)
            if board[i][len(board[0]) - 1] == 'O' and track[i][len(board[0]) - 1] is None:
                self.dfs(board, track, i, len(board[0]) - 1)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    continue
                if track[i][j] is None or track[i][j] == 0:
                    board[i][j] = 'X'
        return board
    
    def dfs(self, board, track, i, j):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return
        if track[i][j] is None:
            if board[i][j] == 'O':
                track[i][j] = 1
            else:
                track[i][j] = 0
                return
        else:
            return
        self.dfs(board, track, i - 1, j)
        self.dfs(board, track, i + 1, j)
        self.dfs(board, track, i, j + 1)
        self.dfs(board, track, i, j - 1)
        return
