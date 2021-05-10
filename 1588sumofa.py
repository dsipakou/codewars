class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        k = 1
        output = 0
        while k <= len(arr):
            for i in range(len(arr) + 1 - k):
                output += sum(arr[i: i + k])
            k += 2
        return output
