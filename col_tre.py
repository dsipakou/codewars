from collections import defaultdict

class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        def dfs(node):
            for child in graph[node]:
                if child in color:
                    if color[child] != 1 - color[node]:
                        return False
                else:
                    color[child] = 1 - color[node]
                    if not dfs(child):
                        return False
            return True
        
        graph = defaultdict(list)
        for v in dislikes:
            graph[v[0]].append(v[1])
            graph[v[1]].append(v[0])
        color = {}
        for k in graph:
            if k not in color:
                color[k] = 0
                if not dfs(k):
                    return False
        return True
