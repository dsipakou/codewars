class Solution:
    def getSum(self, a: int, b: int) -> int:
        xor_temp = a ^ b
        curry = a & b
        if curry == 0:
            return xor_temp
        else:
            return self.getSum(xor_temp, curry << 1)
