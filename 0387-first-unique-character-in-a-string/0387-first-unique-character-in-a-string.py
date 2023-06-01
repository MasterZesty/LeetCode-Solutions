class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        # calculate frequncy hashmap first
        f = {}
        
        for i,v in enumerate(s):
            if v not in f.keys():
                f[v] = 1
            else:
                f[v] += 1
                
        
        # now we have freq hmap then iterate over an arr and check with hmap 
        
        for i,v in enumerate(s):
            if f[v] == 1:
                return i
            
        return -1