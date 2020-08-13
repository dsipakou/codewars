class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        output = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    output += 1
        return output
