class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            return "0"
        for _ in range(k):
            deleted = False
            for j in range(1, len(num)):
                if num[j] < num[j - 1]:
                    num = num[:j - 1] + num[j:]
                    deleted = True
                    break
            if not deleted:
                num = num[:-1]
        return str(int(num))