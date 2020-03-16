def subarraySum(nums, k: int) -> int:
    sums = {}
    output = 0
    cur_sum = 0
    for n in nums:
        cur_sum += n
        if cur_sum == k:
            output += 1
        diff = cur_sum - k
        if diff in sums:
            output += sums[diff]
        sums[cur_sum]  = sums.get(cur_sum, 0) + 1
    return output
print(subarraySum([-1, -1, 1], 0))
