class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_min = nums[0]
        glob_max = curr_max
        for i in range(1, len(nums)):
            prev_min = curr_min
            prev_max = curr_max
            
            curr_min = min(prev_min * nums[i], nums[i], prev_max * nums[i])
            curr_max = max(prev_min * nums[i], nums[i], prev_max * nums[i])
            glob_max = max(curr_max, glob_max)
        return glob_max
