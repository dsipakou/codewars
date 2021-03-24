class Solution:
    def countLargestGroup(self, n: int) -> int:
        d = {}
        for i in range(1, n + 1):
            cur_num_sum = 0
            div = 10
            while i > 0:
                cur_num_sum += i % 10
                i = i // 10
            d[cur_num_sum] = d.get(cur_num_sum, 0)
            d[cur_num_sum] += 1
        t = sorted(d.values(), reverse=True)
        max_num = t[0]
        output = 0
        i = 0
        while i < len(t) and t[i] == max_num:
            output += 1
            i += 1
        return output
