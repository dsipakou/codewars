class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        output = sorted(arr, key=self.strategy)
        return output
    
    def strategy(self, item):
        return bin(item).count('1')
