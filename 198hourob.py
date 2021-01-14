class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 2:
            return max(nums)
        output = [0 for _ in range(len(nums))]
        output[0] = nums[0]
        output[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            output[i] = max(output[i - 1], nums[i] + output[i - 2])
        print(output)
        return output[-1]
