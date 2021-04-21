class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        output = start
        for i in range(n - 1):
            output ^= start + 2
            start += 2
        return output
