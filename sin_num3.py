class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n = {}
        for i in nums:
            if i not in n:
                n[i] = True
            else:
                del n[i]
        output = []
        for k, v in n.items():
            output.append(k)
        return output
