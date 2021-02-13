class NumArray:

    def __init__(self, nums: List[int]):
        self.original = nums[:]
        self.arr = [0, nums[0]]
        for i in range(1, len(nums)):
            self.arr.append(self.arr[i] + nums[i])

    def update(self, index: int, val: int) -> None:
        self.arr[index + 1] = self.arr[index + 1] - self.original[index] + val
        for i in range(index + 1, len(self.original)):
            self.arr[i + 1] = self.arr[i] + self.original[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.arr[right + 1] - self.arr[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
