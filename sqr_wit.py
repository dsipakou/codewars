class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low = 0
        high = num
        while low <= high:
            temp_num = low + (high - low) // 2
            square = temp_num ** 2
            if square == num:
                return True
            elif square > num:
                high = temp_num - 1
            else:
                low = temp_num + 1
        return False


s = Solution()
print(s.isPerfectSquare(16))