from collections import defaultdict

class Solution:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        for ticket in tickets:
            self.graph[ticket[0]].append(ticket[1])
        for key, val in self.graph.items():
            val.sort(reverse=True)
        key = 'JFK'
        self.output = []
        print(self.graph)
        self.dfs(key)
        print(self.output)
        return self.output[::-1]
    
    def dfs(self, node):
        dests = self.graph[node]
        while dests:
            dest = dests.pop()
            self.dfs(dest)
        self.output.append(node)
