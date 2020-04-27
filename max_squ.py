class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        output = 0
        dp = [[0 for _ in range(len(matrix[0])+1)] for _ in range(len(matrix) + 1)]
        for j in range(1, len(matrix) + 1):
            for i in range(1, len(matrix[0]) + 1):
                if matrix[j - 1][i - 1] == '1':
                    dp[j][i] = 1+min(dp[j-1][i], dp[j-1][i-1], dp[j][i-1])
                    output = max(output, dp[j][i])
        print(dp)
        return output * output