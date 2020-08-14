class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        d = {}
        for i, v in enumerate(indices):
            d[v] = s[i]
        return ''.join(d[i] for i in range(len(s)))
