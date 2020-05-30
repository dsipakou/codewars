class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key=lambda item: item[0] ** 2 + item[1] ** 2)
        return points[:K]