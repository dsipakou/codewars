class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        output = []
        for i in range(len(nums) // 2):
            output.append(nums[i])
            output.append(nums[i + len(nums) // 2])
        return output
