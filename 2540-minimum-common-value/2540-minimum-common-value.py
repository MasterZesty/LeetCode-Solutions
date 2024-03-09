class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        min_int = float('inf')
        
        h1 = {}
        h2 = {}
        
        for n1 in nums1:
            h1[n1] = h1.get(n1,0) + 1
            
        for n2 in nums2:
            h2[n2] = h2.get(n2, 0) + 1
            
        
        for n, f in h1.items():
            if h2.get(n, 0) != 0:
                min_int = min(min_int, n)
        
        if min_int != float('inf'):
            return min_int
        
        return -1