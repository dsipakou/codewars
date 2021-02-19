class Solution:
    def maxScore(self, s: str) -> int:
        output = 0
        for i in range(1, len(s)):
            output = max(output, s[:i].count('0') + s[i:].count('1'))
        return output
            
