from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur_max = nums[0]
        index = 0
        while index < len(nums):
            if cur_max == index and nums[index] == 0:
                return False
            cur_max = max(cur_max, index + nums[index])
            index += 1
            if index == len(nums) - 1:
                break
        return True

s = Solution()
print(s.canJump([2,0,0]))