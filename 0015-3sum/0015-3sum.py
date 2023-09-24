class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # aprroch 1 : TC O(n^3) gives TLE
        '''
        ans = []
        n = len(nums)
        
        for i in range(n-2):
            
            for j in range(n-1):
                
                for k in range(n):
                    
                    if i != j and i != k and j != k:
                        
                        if nums[i] + nums[j] + nums[k] == 0:
                            t = [nums[i] , nums[j] , nums[k]]
                            t.sort()
                            
                            if t not in ans:
                                
                                ans.append(t)
                            
        # print(ans)
        return ans
        '''
        
        # approch 2 : reduce TC to O(n^2) by sorting and two pointer
        ans = []
        nums.sort()
        n =len(nums)
        
        for i in range(n-2):
            # skip duplicate values | we can also skip duplictaes by sorting and then checking given combination exists or not
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            l = i + 1
            r = n - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                
                if total == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    
                    # basically skip duplicate elements
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    
                    l += 1
                    r -= 1
                #  sum is too small, and we need to make it larger to get closer to zero. To do this, we increment the left pointer
                elif total < 0:
                    l += 1
                    
                # sum is not negative, and we want to try to reduce it or keep it the same while searching for a triplet sum of zero. To achieve this, we decrement the right pointer 
                else:
                    r -= 1
        return ans
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                            
            