from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for i, v in enumerate(s):
            if counter[v] == 1:
                return i
        return -1
