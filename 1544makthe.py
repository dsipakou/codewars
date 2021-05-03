class Solution:
    def makeGood(self, s: str) -> str:
        if len(s) == 0:
            return s
        output = [s[0],]
        diff = abs(ord('a') - ord('A')) 
        for i in range(1, len(s)):
            if len(output) > 0:
                if abs(ord(output[-1]) - ord(s[i])) != diff:
                    output.append(s[i])
                else:
                    output.pop()
            else:
                output.append(s[i])
        return ''.join(s for s in output)
