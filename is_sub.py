class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s1 = s2 = 0
        while s1 < len(t) and s2 < len(s):
            if s[s2] == t[s1]:
                s2 += 1
            s1 += 1
        return s2 == len(s)
