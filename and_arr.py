class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if len(bin(m)) != len(bin(n)):
            return 0
        return reduce(lambda x, y: x & y, range(m, n + 1))

s = Solution()
print(s.rangeBitwiseAnd(5, 8))