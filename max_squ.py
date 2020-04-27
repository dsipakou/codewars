class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        output = 0
        for j in range(len(matrix)):
            for i in range(len(matrix[0])):
                output = max(output, self.get_deep(matrix, i, j))
        return output * output
    
    def get_deep(self, matrix, i, j):
        if j >= len(matrix) or i >= len(matrix[0]) or matrix[j][i] == "0":
            return 0
        return 1 + min(self.get_deep(matrix, i+1, j), 
                       self.get_deep(matrix, i, j+1), 
                       self.get_deep(matrix, i+1, j+1))