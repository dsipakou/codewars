class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        output = ''
        count = [[a, 'a'], [b, 'b'], [c, 'c']]
        i = j = k = 0
        
        while count[0][0] >= 0 and count[1][0] >= 0 and count[2][0] >= 0:
            count.sort(reverse=True)
            print(count)
            output += count[0][1]
            count[0][0] -= 1
            if output[-1] == count[0][1]:
                i += 1
            else:
                i = 1
            print(i)
        return outputtput
