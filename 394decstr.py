class Solution:
    def __init__(self):
        self.output = ''
        
    def decodeString(self, s: str) -> str:
        i = 0
        while i < len(s):
            if s[i].isdigit():
                subs, i = self.get_str(s, i + 2, int(s[i]))
                self.output += subs
            else:
                self.output += s[i]
            i += 1
            
        return self.output
    
    def get_str(self, s, i=0, repeat=1):
        print(s, i, repeat)
        tmp_str = ''
        index = i
        while s[index] != ']':
            if s[index].isdigit():
                subs, i = self.get_str(s, index + 1, int(s[index]))
                tmp_str += subs
            else:
                tmp_str += s[index]
            index += 1
        return tmp_str * repeat, index
