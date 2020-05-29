from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(node):
            if node in d:
                if d[node] == 'P':
                    return False
                else:
                    return True
            d[node] = 'P'
            if node not in graph:
                d[node] = 'V'
                return True
            for nodes in graph[node]:
                if not dfs(nodes):
                    return False
            d[node] = 'V'
            return True
        d = {}
        graph = {}
        for edge in prerequisites:
            graph[edge[1]] = graph.get(edge[1], [])
            graph[edge[1]].append(edge[0])
        for g in graph:
            if g in d and d[g] == 'V':
                continue
            if not dfs(g):
                return False
        return True

s = Solution()
print(s.canFinish(2, [[0, 1], [1, 0]]))