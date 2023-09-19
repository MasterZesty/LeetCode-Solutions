class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # TC O(n) SC O(n) and this will be constant as max keys in hmap will be n and min 1 
        hmap = {}
        
        for i in nums:
            
            hmap[i] = hmap.get(i,0) + 1
            
            if hmap.get(i,0) > 1:
                
                return i
                
        
        return 0
        