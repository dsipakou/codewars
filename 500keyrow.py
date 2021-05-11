class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        output = []
        for word in words:
            if (
                all(s.lower() in row[0] for s in word) 
                or all(s.lower() in row[1] for s in word)
                or all(s.lower() in row[2] for s in word)
            ):
                output.append(word)
        return output
