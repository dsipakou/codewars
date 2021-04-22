class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        gen_len = sum(wall[0])
        output = len(wall)
        d = {}
        for i in range(len(wall)):
            d[i] = {"index": 0, "value": wall[i][0]}
        for i in range(1, gen_len + 1):
            gaps = 0
            for j in range(len(wall)):
                if d[j]["value"] == 0:
                    gaps += 1
                    d[j]["index"] += 1
                    d[j]["value"] = wall[j][d[j]["index"]]
                else:
                    d[j]["value"] -= 1
            output = min(output, len(wall) - gaps)
        return output
