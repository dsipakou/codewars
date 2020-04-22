# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:




#### O(m*logn)
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        m, n = binaryMatrix.dimensions()
        min_n = n + 1
        for row in range(m):
            left = 0
            right = n - 1
            while left < right:
                pivot = left + (right - left) // 2
                if binaryMatrix.get(row, pivot) == 1:
                    right = pivot
                else:
                    left = pivot + 1
            min_n = min(min_n, right) if binaryMatrix.get(row, right) == 1 else min_n
        return min_n if min_n < n else -1


#### O(n+m)
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        m, n = binaryMatrix.dimensions()
        min_n = n + 1
        v = n - 1
        h = 0
        while h < m and v >= 0:
            if binaryMatrix.get(h, v) == 0:
                h += 1
            else: 
                min_n = v
                v -= 1
        return min_n if min_n < n else -1