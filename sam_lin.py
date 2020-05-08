class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        cc = coordinates
        print(cc)
        if len(cc) < 3:
            return True
        for i in range(2, len(cc)):
            if (cc[0][0] - cc[1][0]) * (cc[i][1] - cc[1][1]) != (cc[i][0] - cc[1][0]) * (cc[0][1] - cc[1][1]):
                return False
        return True
