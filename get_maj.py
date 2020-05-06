class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0)
            d[i] += 1
            if d[i] > len(nums)/2:
                return i
