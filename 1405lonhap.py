class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        output = ''
        count = [[a, 'a'], [b, 'b'], [c, 'c']]
        i = 1
        
        while count[0][0] > 0 or count[1][0] > 0 or count[2][0] > 0:

            count.sort(reverse=True)
            if len(output) > 0 and count[0][1] == output[-1]:
                if i == 2:
                    if count[1][0] > 0:
                        output += count[1][1]
                        count[1][0] -= 1
                        i = 1
                    else:
                        break
                else:
                    output += count[0][1]
                    i += 1
                    count[0][0] -= 1
            else:
                i = 1
                output += count[0][1]
                count[0][0] -= 1
        return output
