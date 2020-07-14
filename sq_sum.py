class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        while i * i <= c:
            j = c - i * i
            if self.bin_search(0, j, j):
                return True
            i += 1
        return False
    
    def bin_search(self, i, j, target):
        if i > j:
            return False
        mid = i + (j - i) // 2
        if mid * mid == target:
            return True
        if mid * mid > target:
            return self.bin_search(i, mid - 1, target)
        return self.bin_search(mid + 1, j, target)
