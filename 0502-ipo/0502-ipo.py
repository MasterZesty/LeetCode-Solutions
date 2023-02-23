class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        n = len(profits)
        project_list = list()  # list of [capital,profit]
        for i in range(n):
            project_list.append([capital[i],profits[i]])
            
        # print(project_list)
        project_list.sort()
        # print(project_list)
        
        from queue import PriorityQueue
        
        pq = PriorityQueue()
        
        j = 0
        for i in range(k):
            while ( j<n and project_list[j][0] <= w ):
                pq.put(-project_list[j][1])
                j += 1
                
            if pq.empty():
                break
                
            temp = -(pq.get())
            #print(temp)
            
            w += temp
            
        return w