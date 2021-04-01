class Solution:
    def average(self, salary: List[int]) -> float:
        if len(salary) < 3:
            return 0
        ssum = sum(salary) - min(salary) - max(salary)
        return ssum / (len(salary) - 2)
