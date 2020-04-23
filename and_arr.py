class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        output = reduce(lambda x, y: x & y, range(m, n + 1))
        return output