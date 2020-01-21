def sort_col(nums):
    for i in range(len(nums), 1, -1):
        for j in range(1, i):
            if nums[j - 1] > nums[j]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
    return nums
