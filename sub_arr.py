class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = {}
        summ = 0
        output = 0
        for i in range(len(nums)):
            summ += nums[i]
            if summ == k:
                output += 1
            to_find = summ - k
            if to_find in sums:
                output += sums[to_find]
            sums[summ] = sums.get(summ, 0)
            sums[summ] += 1
        return output