class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        from collections import deque
        
        q = deque()
        
        for i in range(1, n+1):
            q.append(i)
            
        # print(q)
        
        t = k
        while len(q) > 1:
            
            p = q.popleft()
            t -= 1
            if t == 0:
                t = k
            else:
                q.append(p)
            
            # print(f"q: {q} | p:{p}")
        
        
        return q.pop()