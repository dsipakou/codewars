class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        cur_min = float('inf')
        cur_sum = 0
        for num in nums:
            cur_sum += num
            cur_min = min(cur_min, cur_sum)
        return max(1 - cur_min, 1)
