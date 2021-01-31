class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        start = 0
        while 3 ** start < n:
            start += 1
        return n == 3 ** start
