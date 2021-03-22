from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        output = 0
        add = False
        has_carry = False
        d = Counter(s)
        for k, v in d.items():
            if v == 1 and not add:
                output += 1
                add = True
            else:
                output += v // 2 * 2
                if v % 2:
                    has_carry = True
        if not add and has_carry:
            output += 1
        return output
