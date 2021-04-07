class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        output = 0
        for i in range(len(s) // 2):
            if self.is_vowel(s[i]):
                output += 1
        for i in range(len(s) // 2, len(s)):
            if self.is_vowel(s[i]):
                output -= 1
        return output == 0
    
    def is_vowel(self, char: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u']
        return char.lower() in vowels
