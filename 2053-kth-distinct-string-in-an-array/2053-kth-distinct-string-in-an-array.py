class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hm = {}
        
        for i,v in enumerate(arr):
            hm[v] = hm.get(v, 0) + 1
            
        ans = ""
        for ky, val in hm.items():
            if val == 1:
                k -= 1
                
            if  k == 0:
                ans = ky
                break
                
        return ans