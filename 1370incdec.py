class Solution:
    def sortString(self, s: str) -> str:
        d = {}
        for c in s:
            d[c] = d.get(c, 0)
            d[c] += 1
        sorted_d = sorted(d.items())
        count = len(s)
        dirr = 0
        i = 0
        output = ''
        while count > 0:
            if dirr == 0:
                if i == len(sorted_d) - 1:
                    if sorted_d[i][1] > 0:
                        output += sorted_d[i][0]
                        sorted_d[i] = (sorted_d[i][0], sorted_d[i][1] - 1)
                    dirr = 1
                else:
                    if sorted_d[i][1] > 0:
                        output += sorted_d[i][0]
                        sorted_d[i] = (sorted_d[i][0], sorted_d[i][1] - 1)
                    i += 1
            else:
                if i == 0:
                    if sorted_d[i][1] > 0:
                        output += sorted_d[i][0]
                        sorted_d[i] = (sorted_d[i][0], sorted_d[i][1] - 1)
                    dirr = 0
                else:
                    if sorted_d[i][1] > 0:
                        output += sorted_d[i][0]
                        sorted_d[i] = (sorted_d[i][0], sorted_d[i][1] - 1)
                    i -= 1
            print(sorted_d)
            count -= 1
        return output
            
