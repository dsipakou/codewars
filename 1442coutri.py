class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        output = 0
        for outer in range(len(arr)):
            a = 0
            for i in range(outer, len(arr) - 1):
                a ^= arr[i]
                b = 0
                for j in range(i + 1, len(arr)):
                    b ^= arr[j]
                    if a == b:
                        output += 1
        return output
