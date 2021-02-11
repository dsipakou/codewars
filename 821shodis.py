class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        arr = [float('inf') for _ in range(len(s))]
        cur_dis = float('inf')
        for i in range(len(s)):
            if s[i] == c:
                arr[i] = 0
            elif i > 0:
                arr[i] = arr[i - 1] + 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == c:
                cur_dis = 0
            elif cur_dis < float('inf'):
                cur_dis += 1
            arr[i] = min(arr[i], cur_dis)
        return arr
                
