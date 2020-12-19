class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        arr = list(range(1, m + 1))
        output = []
        for q in queries:
            idx = arr.index(q)
            output.append(idx)
            for j in reversed(range(1, idx + 1)):
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
        return output
