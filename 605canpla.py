class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        available = True
        cnt = 0
        for i in range(len(flowerbed) - 1):
            if flowerbed[i] == 1:
                available = False
                continue
            if not available:
                available = True
                continue
            if flowerbed[i + 1] == 0:
                cnt += 1
                available = False
        if flowerbed[-1] == 0 and available:
            cnt += 1
        return cnt >= n
