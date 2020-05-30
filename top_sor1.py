def topologicalSort(jobs, deps):
    def dfs(node):
        if node in visited:
            if visited[node] == 'P':
                return False
            else:
                return
        visited[node] = 'P'
        for child in graph.get(node):
            if dfs(child) is False:
                return False
        visited[node] = 'V'
        output.append(node)

    visited = {}
    graph = {k: [] for k in jobs}
    output = []
    for dep in deps:
        graph[dep[1]].append(dep[0])
    for i in graph:
        if i in visited:
            continue
        if dfs(i) is False:
            return []
    return output

print(topologicalSort([1, 2, 3, 4], [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]))
