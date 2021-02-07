class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.arr = []
        for i in range(len(matrix)):
            cur = 0
            temp = [0]
            for j in range(len(matrix[0])):
                cur += matrix[i][j]
                temp.append(cur)
            self.arr.append(temp)
            temp = []        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        output = 0
        for i in range(row1, row2 + 1):
            divv = self.arr[i][col2+1] - self.arr[i][col1]
            output += divv
        return output
