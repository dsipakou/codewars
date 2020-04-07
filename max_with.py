class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_with_stock = 0
        max_without_stock = float('-inf')
        for x in prices:
            max_without_stock = max(max_without_stock, max_with_stock - x)
            max_with_stock = max(max_with_stock, max_without_stock + x)
        return max_with_stock