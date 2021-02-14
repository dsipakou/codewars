class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        output = 0
        s_num = str(num)
        while len(s_num) > 1:
            for i in range(len(s_num)):
                output += int(s_num[i])
            s_num = str(output)
            output = 0
        return int(s_num)
