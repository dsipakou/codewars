class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        loc_sum = sum(nums)
        glo_sum = sum([i for i in range(len(nums) + 1)])
        return glo_sum - loc_sum
