class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        hmap = {}
        
        for i in nums:
            
            hmap[i] = hmap.get(i,0) + 1
            
            if hmap.get(i,0) > 1:
                
                return i
                
        
        return 0
        