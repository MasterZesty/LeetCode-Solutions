class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        count_n1 = 0
        count_n2 = 0
        
        len_n1 = len(nums1)
        len_n2 = len(nums2)
        
        hm_n1 = {}
        hm_n2 = {}
        
        for i in range(len_n1):
            
            hm_n1[ nums1[i] ] = hm_n1.get(nums1[i],0) + 1

        for i in range(len_n2):
            
            hm_n2[ nums2[i] ] = hm_n2.get(nums2[i],0) + 1
                
        for i in range(len_n1):
            
            if hm_n2.get( nums1[i], 0) != 0:
                count_n1 += 1
                
        for i in range(len_n2):
            
            if hm_n1.get( nums2[i], 0) != 0:
                count_n2 += 1
                
        return [count_n1, count_n2]
    