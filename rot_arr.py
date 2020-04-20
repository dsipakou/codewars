class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        left = 0
        right = len(nums)
        pivot = 0
        while left < right:
            piv = left + (right - left) // 2
            if left == piv:
                pivot = right
                break
            if nums[piv] > nums[0]:
                left = piv
            else:
                right = piv
        left = 0
        right = len(nums) - 1
        if target == nums[0]:
            return 0
        if target > nums[0]:
            right = pivot - 1
        else:
            left = pivot
        while left <= right:
            piv = left + (right - left) // 2
            if nums[piv] > target:
                right = piv - 1
            else:
                left = piv + 1
        return right if nums[right] == target else -1