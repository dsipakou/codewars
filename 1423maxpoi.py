class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        global_max = 0
        if k >= len(cardPoints):
            return sum(cardPoints)
        for i in range(k + 1):
            current_sum = sum(cardPoints[: k - i]) + sum(cardPoints[len(cardPoints) - i:])
            global_max = max(global_max, current_sum)
        return global_max
