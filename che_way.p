import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(set)
        for i,j,w in flights:
            graph[i].add((j, w))
        
        cost = {}
        cost[src] = 0
        
        heap = self.build_heap(graph, src)
        cost = self.find_cost(graph, heap, {}, src, K)
        return -1 if dst not in cost else cost[dst]
    
    def build_heap(self, graph, src):
        heap = []
        for k, v in graph[src]:
            heapq.heappush(heap, (0, k, v))
        return heap
    
    def find_cost(self, graph, heap, cost, src, k):    
        while heap:
            stop, src, c = heapq.heappop(heap)
            if src not in cost or c < cost[src]:
                cost[src] = c
                if stop < k:
                    for j,w in graph[src]:
                        heapq.heappush(heap, (stop+1, j, c+w))
        return cost
                
            
        
