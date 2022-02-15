class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [['' for _ in range(len(text1) + 1)] for _ in range(len(text2) + 1)]
        for i in range(len(text2)):
            for j in range(len(text1)):
                if text1[j] == text2[i]:
                    dp[i + 1][j + 1] = dp[i][j] + text1[j]
                else:
                    dp[i + 1][j + 1] = dp[i][j + 1]
                    if len(dp[i + 1][j + 1]) < len(dp[i + 1][j]):
                        dp[i + 1][j + 1] = dp[i + 1][j]
        return len(dp[-1][-1])
