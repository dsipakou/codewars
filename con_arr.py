class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {0: -1}
        count = 0
        output = 0
        for i, v in enumerate(nums):
            if v == 0:
                count += -1
            else:
                count += 1
            if count in d:
                output = max(output, i - d[count])
            else:
                d[count] = i
        return output