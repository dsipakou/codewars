class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        print(s1, s2)
        d = {}
        for i in s1:
            d[i] = d.get(i, 0) + 1
        find = 0
        for i in range(len(s2)):
            if s2[i] in d:
                d[s2[i]] -= 1
                if d[s2[i]] == 0:
                    find += 1
            if i >= len(s1):
                if s2[i - len(s1)] in d:
                    d[s2[i - len(s1)]] += 1
                    if d[s2[i - len(s1)]] == 1:
                        find -= 1
            if find == len(d):
                return True
        return False
