class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        d = {}
        while left < len(nums):
            if target - nums[left] not in d:
                d[nums[left]] = left
            else:
                break
            left += 1
        return [left, d[target-nums[left]]]
