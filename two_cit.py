class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        lth = len(costs)
        output = 0
        for i in range(lth//2):
            output += costs[i][0]
        for i in range(lth//2, lth):
            output += costs[i][1]
        return output
