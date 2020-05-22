from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        d = Counter(s)
        output = ''
        d = {k: v for k, v in reversed(sorted(d.items(), key=lambda item: item[1]))}
        for c, v in d.items():
            output += c * v
        return output
