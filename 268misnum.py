class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        loc_sum = 0
        glo_sum = 0
        flag = False
        for i, v in enumerate(nums):
            glo_sum += i
            if v == len(nums):
                flag = True    
                glo_sum += v
            loc_sum += v
        ret = glo_sum - loc_sum
        if ret == 0 and not flag:
            return len(nums)
        return ret
