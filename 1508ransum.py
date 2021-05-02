class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        new_arr = []
        for i, v in enumerate(nums):
            new_arr.append(v)
            cur_num = v
            for j in range(i + 1, len(nums)):
                cur_num += nums[j]
                new_arr.append(cur_num)
        new_arr.sort()
        return sum(new_arr[left -1: right])%(10**9+7)
