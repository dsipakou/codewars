from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = Counter(arr)
        output = -1
        for k, v in d.items():
            if k == v:
                output = max(output, v)
        return output
