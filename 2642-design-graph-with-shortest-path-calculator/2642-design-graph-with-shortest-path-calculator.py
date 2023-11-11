class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        # represent the edge/node and cost with data structure
        # array 0 to n
        self.adj = [[] for i in range(n)]
        
        # add edges to adjacency list
        for edge in edges:
            self.addEdge(edge)

    def addEdge(self, edge: List[int]) -> None:
        # add edges to graph through adjacency list
        self.adj[edge[0]].append( [ edge[1], edge[2] ] )
        

    def shortestPath(self, node1: int, node2: int) -> int:
        # shortest path from n1 to n2
        # print(f'adj : {self.adj} node 1 : {node1} node 2 {node2}')
        return self.dijkstra(node1, node2)
    
    def dijkstra(self, start: int, end: int) -> int:
        n = len(self.adj)
        distances = [float('inf')]*n
        distances[start] = 0
        
        
        # p queue to retrive min distance
        priorityQueue = [(0,start)]
        
        while priorityQueue:
            currentCost, currentNode = heapq.heappop(priorityQueue)
            
            # skip shorter path already found
            if currentCost > distances[currentNode]:
                continue
            
            # Explore neighbors and update distances
            for edge in self.adj[currentNode]:
                neighbor, edgecost = edge
                
                newRouteCost = edgecost + distances[currentNode]
                
                if distances[neighbor] > newRouteCost:
                    distances[neighbor] = newRouteCost
                    heapq.heappush(priorityQueue,(newRouteCost, neighbor))
                    
        # Return the minimum distance or -1 if no path exists
        return -1 if distances[end] == float('inf') else distances[end]


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)