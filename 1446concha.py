class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) == 0:
            return 0
        output = 1
        curr = s[0]
        cur_max = 1
        for i in range(1, len(s)):
            if s[i] == curr:
                cur_max += 1
            else:
                output = max(output, cur_max)
                cur_max = 1
                curr = s[i]
        return max(output, cur_max)
