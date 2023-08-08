class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        ans = 0
        
        # approch 1 : brute force approch
        # TC O(n^4) this will give you TLE even for smller values of n
#         for i in range(len(nums1)):
            
#             for j in range(len(nums2)):
                
#                 for k in range(len(nums3)):
                    
#                     for l in range(len(nums4)):
                        
#                         if nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0:
#                             #print(i,j,k,l)
#                             ans += 1
                            
        # approch 2: using hmap of 4th array TC reduced to O(n^3)
#         hm4 = {}
#         for i,val in enumerate(nums4):
#             hm4[val] = hm4.get(val,0) + 1
            
#         for i in range(len(nums1)):
            
#             for j in range(len(nums2)):
                
#                 for k in range(len(nums3)):
                    
#                     t = nums1[i] + nums2[j] + nums3[k]
                    
#                     if hm4.get(-t,0) !=0:
#                         # print(i,j,k,'--',hm4[-t])
#                         ans += hm4[-t]
                        
                        
        # approch 3
        hm = {}
        for i in range(len(nums1)):
            
            for j in range(len(nums2)):
                
                hm[nums1[i]+nums2[j]] = hm.get(nums1[i]+nums2[j],0) + 1
        #print(f'hashmap of arr1 and arr2 : {hm}')        
        
        for k in range(len(nums3)):
            
            for l in range(len(nums4)):
                
                #print(f'nums3[k]+nums4[l] : {nums3[k]+nums4[l]}')
                if hm.get(-(nums3[k]+nums4[l]),0) != 0:
                    #print('adding ' , hm.get(-(nums3[k]+nums4[l]),0))
                    ans += hm.get(-(nums3[k]+nums4[l]),0)
        
                            
                            
        return ans