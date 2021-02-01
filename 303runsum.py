class NumArray:
    __slots__ = 'arr', 

    def __init__(self, nums: List[int]):
        self.arr = [0 for _ in range(len(nums) + 1)]
        for i in range(1, len(self.arr)):
            self.arr[i] = self.arr[i - 1] + nums[i - 1]
        

    def sumRange(self, i: int, j: int) -> int:
        return self.arr[j + 1] - self.arr[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
