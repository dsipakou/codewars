from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero = -1
        number = 0 
        while number < len(nums):
            if nums[number] == 0 and zero == -1:
                zero = number
            if nums[number] != 0 and zero < number and zero != -1:
                nums[number], nums[zero] = nums[zero], nums[number]
                zero += 1
            number += 1
                
        return nums
                

s = Solution()
print(s.moveZeroes([1,0,1]))