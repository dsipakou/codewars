class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        z = str(bin(z))
        output = 0
        for i in range(len(z)):
            if z[i] == '1':
                output += 1
        return output
