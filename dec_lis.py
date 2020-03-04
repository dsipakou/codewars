def decl(nums):
    output = []
    for i in range(0, len(nums), 2):
        output.extend([nums[i + 1]] * nums[i])
    return output

print(decl([1,2,3,4]))
