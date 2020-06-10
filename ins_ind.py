class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums = [float('-inf')] + nums + [float('inf')]
        print(nums)
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid - 1
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return right - 1
