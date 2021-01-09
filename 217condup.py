class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = dict()
        i = 0
        while i < len(nums):
            if nums[i] in d:
                return True
            d[nums[i]] = True
            i += 1
        return False
