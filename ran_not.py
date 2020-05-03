class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if i not in magazine:
                return False
            else:
                idx = magazine.index(i)
                magazine = magazine[:idx] + magazine[idx + 1:]
        return True
