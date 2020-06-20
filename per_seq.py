 class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        levels = []
        nums = [None] * (n+1)
        print(nums)
        res = ""
        k -= 1
        for i in range(2, n+1):
            levels.append(k%i)
            k = k // i

        levels.append(0)
        levels.reverse()
        print(levels)

        for i in range(0, n):
            nums[i] = i+1
            
        print(nums)

        for i in range(1, n):
            j = levels[i]
            res += str(nums[j])
            print(res)
            nums.pop(j)

        res += str(nums[0])
        return res
