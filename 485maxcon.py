class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        output = 0
        curr = 0
        for i, v in enumerate(nums):
            if v == 1:
                curr += 1
            else:
                output = max(output, curr)
                curr = 0
        return max(output, curr)
