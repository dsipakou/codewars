class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        d = {k: [0, 0] for k in range(1, N+1)}
        for i in trust:
            d[i[0]][0] += 1
            d[i[1]][1] += 1
        output = -1
        for k, v in d.items():
            if v[0] == 0 and v[1] == N - 1:
                if output == -1:
                    output = k
                else:
                    return -1
        return output