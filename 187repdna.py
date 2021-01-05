class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        found = set()
        seen = dict()
        left = 0
        while left <= len(s) - 10:
            if not seen.get(s[left: left + 10]):
                seen[s[left: left + 10]] = True
            else:
                found.add(s[left: left + 10])
            left += 1
        return list(found)
