class Solution:
    def countSegments(self, s: str) -> int:
        ss = s.split(' ')
        output = 0
        for i in ss:
            if i != '':
                output += 1
        return output
