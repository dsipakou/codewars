class Solution:
    def reverseBits(self, n: int) -> int:
        return int(bin(n)[2:][::-1], base=2)
