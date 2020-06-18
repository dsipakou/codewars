class Solution:
    def hIndex(self, citations: List[int]) -> int:
        output = 0
        for i in range(len(citations)):
            if citations[i] >= len(citations) - i:
                output = len(citations) - i
                break
        return output
