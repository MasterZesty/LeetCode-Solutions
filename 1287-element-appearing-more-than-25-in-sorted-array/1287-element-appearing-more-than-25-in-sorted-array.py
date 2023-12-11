class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        n = len(arr)
        
        t = int(n*0.25)
        
        print(f"n: {n} t:{t}")
        
        hm = {}
        
        ans = 0
        t_max = 0
        
        for i,v in enumerate(arr):
            
            hm[v] = hm.get(v,0) + 1
            
            if t_max < hm.get(v,0):
                t_max = hm[v]
                ans = v
        
        return ans