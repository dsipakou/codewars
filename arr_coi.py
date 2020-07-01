class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n
        while l <= r:
            pivot = (l + r) // 2
            curr = pivot * (pivot + 1) // 2
            if curr == n:
                return pivot
            if curr > n:
                r = pivot - 1
            else:
                l = pivot + 1
        return r
