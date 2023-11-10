class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:

        # Approach 1: Depth-First Search (DFS)
        graph = defaultdict(list)
        
        for x ,y in adjacentPairs:
            graph[x].append(y)
            graph[y].append(x)
            
        #print(f'graph : {graph}')
        
        
        # find root to travel from
        root = None
        for num in graph:
            if len(graph[num]) == 1:
                root = num
                break
                
        def dfs(node, prev, ans):
            ans.append(node)
            for neighbor in graph[node]:
                if neighbor != prev:
                    dfs(neighbor, node, ans)
                    
        ans = []
        dfs(root,None,ans)
        
        return ans