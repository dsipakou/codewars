class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        output = s[0]
        i = 0
        while i < len(s):
            left = right = i
            cur = self.get_pal(s, left, right)
            if len(cur) > len(output):
                output = cur
            if right < len(s) - 1:
                if s[left] == s[right + 1]:
                    if len(output) < 2:
                        output = s[left:right + 2]
                    cur = self.get_pal(s, left, right + 1)
                    if len(cur) > len(output):
                        output = cur
            i += 1
        return output

    def get_pal(self, s, left, right):
        output = ""
        while left > 0 and right < len(s) - 1:
            if s[left - 1] == s[right + 1]:
                left -= 1
                right += 1
            else:
                break
        return s[left: right + 1]
