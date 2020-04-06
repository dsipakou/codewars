from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_list = [''.join(sorted(s)) for s in strs]
        d = defaultdict(list)
        for i, v in enumerate(sorted_list):
            d[v].append(strs[i])
        return [d[key] for key in d.keys()]

s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))