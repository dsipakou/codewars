class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows, cols = len(dungeon), len(dungeon[0])
        dp = [[float('inf')] * cols for _ in range(rows)]
        dp[rows - 1][cols - 1] = (max(1, 1 - dungeon[rows - 1][cols - 1]), None)
        for row in reversed(range(rows)):
            for col in reversed(range(cols)):
                if col < cols - 1 and row < rows - 1:
                    if dp[row + 1][col][0] < dp[row][col + 1][0]:
                        dp[row][col] = (max(1, dp[row + 1][col][0] - dungeon[row][col]), 'DOWN')
                    else:
                        dp[row][col] = (max(1, dp[row][col + 1][0] - dungeon[row][col]), 'RIGHT')
                else:
                    if col == cols - 1 and row < rows - 1:
                        dp[row][col] = (max(1, dp[row + 1][col][0] - dungeon[row][col]), 'DOWN')
                    if row == rows - 1 and col < cols - 1:
                        dp[row][col] = (max(1, dp[row][col + 1][0] - dungeon[row][col]), 'RIGHT')

        return dp[0][0][0]
