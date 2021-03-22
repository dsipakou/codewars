class Solution:
    def longestPalindrome(self, s: str) -> int:
        output = 0
        for i in range(1, len(s)):
            left = right = i
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    output = max(output, right - left + 1)
                    left -= 1
                    right += 1
                else:
                    break
            left = i - 1
            right = i
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    output = max(output, right - left + 1)
                    left -= 1
                    right += 1
                else:
                    break
        return output
