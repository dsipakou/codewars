class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        output = []
        d = {}
        for c in p:
            d[c] = d.get(c, 0) + 1
        find = 0
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] -= 1
                if d[s[i]] == 0:
                    find += 1
                
            if i >= len(p):
                if s[i - len(p)] in d:
                    d[s[i - len(p)]] += 1
                    if d[s[i - len(p)]] == 1:
                        find -= 1
            if find == len(d):
                output.append(i - len(p) + 1)
        return output
