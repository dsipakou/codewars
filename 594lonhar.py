from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums = Counter(nums)
        output = 0
        for k, v in nums.items():
            if k + 1 in nums:
                output = max(output, nums[k] + nums[k + 1])
        return output
