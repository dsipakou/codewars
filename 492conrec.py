import math

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        pivot = int(math.sqrt(area))
        while pivot > 1:
            if area % pivot == 0:
                return [area // pivot, pivot]
            pivot -= 1
        return [area, pivot]
