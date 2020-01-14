def sequence(n):
    f_nums = {1, 2}
    output = []
    if n < 2:
        return n
    current_num = 3
    for i in range(2, n + 1):
        print(i)
        while current_num in f_nums:
            current_num += 1
        tmp_num = []
        print("Before: ", f_nums)
        for j in f_nums:
            print("Current j", j)
            print("Current j + current_num", current_num + (current_num - j))
            tmp_num.append(current_num + j)
        f_nums.update(tmp_num)
        f_nums.add(current_num)
        f_nums.add(current_num * 2)
        print("After: ", f_nums)
    return current_num


print(sequence(2))
