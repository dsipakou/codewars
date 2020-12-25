class Solution:
    def titleToNumber(self, s: str) -> int:
        output = 0
        for i in range(len(s)):
            output += (ord(s[i]) - 64) * (26 ** (len(s) - i - 1))
        return output
