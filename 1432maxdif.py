class Solution:
    def maxDiff(self, num: int) -> int:
        str_num: list = list(str(num))
        max_num: list = str_num[:]
        min_num: list = str_num[:]
        x: str = ''
        y: str = ''
        skip_one: bool = False
        min_n: str = '0'
        for i in range(len(str_num)):
            if max_num[i] == '9':
                continue
            if x == '':
                x = max_num[i]
            if max_num[i] == x:
                max_num[i] = '9'
        for i in range(len(min_num)):
            if min_num[i] == '1' and i == 0:
                skip_one = True
                continue
            if min_num[i] == '0' or (min_num[i] == '1' and skip_one):
                continue
            if y == '':
                y = min_num[i]
            if i == 0:
                min_n = '1'
            if min_num[i] == y:
                min_num[i] = min_n
        return int(''.join(str(s) for s in max_num))-int(''.join(str(s) for s in min_num))
            
                
