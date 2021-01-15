class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        sources = []
        targets = []
        for path in paths:
            sources.append(path[0])
            targets.append(path[1])
        for t in targets:
            if t not in sources:
                return t
