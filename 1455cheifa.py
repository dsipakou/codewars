class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, word in enumerate(sentence.split(), 1):
            if len(word) >= len(searchWord) and word[:len(searchWord)] == searchWord:
                return i
        return -1
