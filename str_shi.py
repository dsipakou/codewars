class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        num_of_shifts = 0
        for ss in shift:
            if ss[0] == 0:
                num_of_shifts -= ss[1]
            else:
                num_of_shifts += ss[1]
        if num_of_shifts == 0:
            return s
        else:
            return s[-num_of_shifts:] + s[:-num_of_shifts]