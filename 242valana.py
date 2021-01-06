class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = dict()
        for ch in s:
            first[ch] = first.get(ch, 0) + 1
        for ch in t:
            if ch in first:
                first[ch] -= 1
                if first[ch] < 0:
                    return False
            else:
                return False
        for v in first.values():
            if v > 0:
                return False
        return True
