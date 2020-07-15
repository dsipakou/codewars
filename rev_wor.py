class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        return ' '.join(ss for ss in reversed(s))
