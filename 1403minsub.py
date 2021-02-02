class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        ov_sum = sum(nums)
        cur_sum = nums[0]
        index = 0
        while cur_sum <= ov_sum - cur_sum:
            index += 1
            cur_sum += nums[index]
        return nums[:index + 1]
        
