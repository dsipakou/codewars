class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        output = 0
        for i in range(len(arr1)):
            if all([abs(x - arr1[i]) > d for x in arr2]):
                output += 1
        return output
