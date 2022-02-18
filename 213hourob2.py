class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0] * (len(nums) + 1)
        
        for i in range(len(nums) - 1):
            dp[i + 2] = max(dp[i + 1], nums[i] + dp[i])
        output1 = dp[-1]
        dp = [0] * (len(nums) + 1)
        
        for i in range(len(nums) - 1):
            dp[i + 2] = max(dp[i + 1], nums[i + 1] + dp[i])
        return max(output1, dp[-1])
