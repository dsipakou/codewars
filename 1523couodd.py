class Solution:
    def countOdds(self, low: int, high: int) -> int:
        output = (high - low) // 2
        if high % 2 == 1 and low % 2 == 1:
            return output + 1
        if low % 2 == 1 or high % 2 == 1:
            return output + 1
        return output
