class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        return str(int(''.join(str(s) for s in self.merge_sort(nums))))
    
    def merge_sort(self, nums):
        if len(nums) < 2:
            return nums
        pivot = len(nums) // 2
        left = self.merge_sort(nums[:pivot])
        right = self.merge_sort(nums[pivot:])
        l = 0
        r = 0
        output = []
        while l < len(left) and r < len(right):
            if int(str(left[l]) + str(right[r])) > int(str(right[r]) + str(left[l])):
                output.append(left[l])
                l += 1
            else:
                output.append(right[r])
                r += 1
        output.extend(left[l:])
        output.extend(right[r:])
        return output
