class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k >= len(cardPoints):
            return sum(cardPoints)
        global_sum = sum(cardPoints[: k])
        global_max = global_sum
        left_sum = global_sum
        right_sum = 0
        for i in range(k):
            left_sum -= cardPoints[k - 1 - i]
            right_sum += cardPoints[0 - 1 - i]
            global_max = max(global_max, (left_sum + right_sum))
        return global_max
    
