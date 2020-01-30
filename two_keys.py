class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        i = 2
        while i <= n:
            if n % i == 0:
                temp = self.minSteps(n // i)
                break
        res = temp
        return temp

s = Solution()
print(s.minSteps(15))