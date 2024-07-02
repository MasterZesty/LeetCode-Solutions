class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mn1 = {}
        mn2 = {}
        
        n1 = len(nums1)
        n2 = len(nums2)
        
        for n in range(n1):
            mn1[nums1[n]] = mn1.get(nums1[n], 0) + 1
            
        for n in range(n2):
            mn2[nums2[n]] = mn2.get(nums2[n], 0) + 1
            
        ans = []
        
        for num, freq in mn1.items():
            if mn2.get(num, 0) != 0:
                min_f = min(mn2[num], mn1[num])
                ans += [num]*min_f
                
                
        return ans