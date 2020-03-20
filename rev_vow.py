class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        tmp = []
        for c in s:
            if c.lower() in vowels:
                tmp.append(c)
        tmp1 = list(s)
        for i, v in enumerate(s):
            if v.lower() in vowels:
                tmp1[i] = tmp.pop()
        return ''.join(s for s in tmp1)
