class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        occofxati = {}
        occ = 1
        for i,v in enumerate(nums):
            
            if v == x:
                occofxati[occ] = i
                occ += 1
        
        
        n = len(queries)
        ans = [-1 for _ in range(n)]
        
        for i,q in enumerate(queries):
            
            if occofxati.get(q, -1) != -1:
                ans[i] = occofxati[q]
                
        
        return ans
        