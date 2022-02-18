class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0] * (len(nums) + 2)
        for i, v in enumerate(nums):
            dp[i + 2] = max(dp[i + 1], dp[i] + v)
        return dp[-1]
