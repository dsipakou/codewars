class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        new_m = []
        for i in range(len(matrix[0])):
            row = []
            for j in range(len(matrix)):
                row.append(matrix[j][i])
            new_m.append(row)
        output = []
        for i, v in enumerate(matrix):
            min_idx = v.index(min(v))
            if max(new_m[min_idx]) == v[min_idx]:
                output.append(v[min_idx])
        return output
