from collections import defaultdict 

class Solution:
    def countElements(self, arr: List[int]) -> int:
        d = defaultdict(int)
        for a in arr:
            d[a] += 1
        output = 0
        for a in arr:
            if d[a + 1] > 0:
                output += 1
        return output