class Solution:
    def getSum(self, a: int, b: int) -> int:
        bin_a = bin(a)[2:]
        bin_b = bin(b)[2:]
        bin_output = []
        max_len = max(len(bin_a), len(bin_b))
        bin_a = bin_a.rjust(max_len, '0')
        bin_b = bin_b.rjust(max_len, '0')
        curry = False
        for i in range(len(bin_a) - 1, -1, -1):
            if bin_a[i] == '1' or bin_b[i] == '1':
                if bin_a[i] == bin_b[i]:
                    if curry:
                        bin_output.append('1')
                    else:
                        bin_output.append('0')
                    curry = True
                else:
                    if curry:
                        bin_output.append('0')
                    else:
                        bin_output.append('1')
            else:
                print('else')
                if curry:
                    bin_output.append('1')
                else:
                    bin_output.append('0')
                curry = False
        if curry:
            bin_output.append('1')
        return int(''.join(i for i in reversed(bin_output)), base=2)
