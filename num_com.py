class Solution:
    def findComplement(self, num: int) -> int:
        llen = len(bin(num)[2:])
        mask = int(''.join('1' for _ in range(llen)), base=2)
        return num ^ mask