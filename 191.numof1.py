class Solution:
    def hammingWeight(self, n: int) -> int:
        return (bin(n)[2:].count('1'))

## With bitwise ops

class Solution:
    def hammingWeight(self, n: int) -> int:
        output = 0
        for _ in range(32):
            if n & 1:
                output += 1
            n = n >> 1
        return output
