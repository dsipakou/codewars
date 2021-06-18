class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            curr = nums[i]
            cur_min = float('inf')
            for j in range(i + 1, i + len(nums)):
                curr_index = j % len(nums)
                if nums[curr_index] > curr:
                    cur_min = min(cur_min, nums[curr_index])
                    break
            if cur_min == float('inf'):
                output.append(-1)
            else:
                output.append(cur_min)
        return output
