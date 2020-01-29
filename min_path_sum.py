class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        output = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                temp = grid[i][j]
                if i > 0 and j > 0:
                    temp = grid[i][j] + min(output[i - 1][j], output[i][j - 1])
                elif i > 0:
                    temp += output[i - 1][j]
                elif j > 0:
                    temp += output[i][j - 1]
                else:
                    temp = grid[i][j]
                output[i][j] = temp
        return output[-1][-1]
