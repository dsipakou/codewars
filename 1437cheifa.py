class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if len(nums) == 0:
            return True
        cur = 0
        if 1 in nums:
            start = nums.index(1) + 1
            for i in range(start, len(nums)):
                if nums[i] == 1:
                    if cur < k:
                        return False
                    else:
                        cur = 0
                else:
                    cur += 1
        return True
