class Solution:
    def findMin(self, nums: List[int]) -> int:
        r = len(nums) - 1
        if nums[0] < nums[r]:
            return nums[0]
        return self.sol(0, r, nums)
    
    def sol(self, left, right, nums):
        if left >= right:
            return nums[left]
        pivot = left + ((right - left) // 2)
        if nums[pivot] >= nums[left] and nums[pivot] > nums[right]:
            return self.sol(pivot + 1, right, nums)
        return self.sol(left, pivot, nums)
            
