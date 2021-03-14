class Solution:
    def __init__(self):
        self.output = ''
        
    def decodeString(self, s: str) -> str:
        output, _ = self.decString(s)
        return output
    
    def decString(self, s, index=0, repeat=1):
        output = ''
        tmpNum = ''
        while index < len(s):
            if s[index].isnumeric():
                tmpNum += s[index]
            elif s[index].isalpha():
                output += s[index]
            elif s[index] == '[':
                tmp, index = self.decString(s, index + 1, int(tmpNum))
                tmpNum = ''
                output += tmp
            else:
                return output * repeat, index
            index += 1
        return output, index
