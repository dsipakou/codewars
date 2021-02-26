class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pat_c = {}
        pat_w = {}
        s = s.split()
        
        if len(pattern) != len(s):
            return False
        
        for c, w in zip(pattern, s):
            if c not in pat_c:
                if w in pat_w:
                    return False
                pat_c[c] = w
                pat_w[w] = c
            else:
                if pat_c[c] != w:
                    return False
        return True
