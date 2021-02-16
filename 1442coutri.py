class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        output = 0
        for i in range(len(arr)):
            a = arr[i]
            for k in range(i + 1, len(arr)):
                a ^= arr[k]
                if a == 0:
                    output += k - i
        return output
