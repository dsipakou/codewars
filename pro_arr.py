class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1:
            return [0 for _ in nums]
        prod = 1
        for i in nums:
            if i != 0:
                prod *= i
        if 0 in nums:
            output = [0 for _ in nums]
            output[nums.index(0)] = prod
            return output
        output = []
        for i in nums:
            if i != 0:
                output.append(prod // i)
            else:
                output.append(0)
        return output