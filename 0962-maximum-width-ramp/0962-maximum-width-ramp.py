class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        '''
        Approch 1: Brute force method
        
        TC : O(n^2)
        SC : O(1)
        '''
        
#         n = len(nums)
#         max_w_ramp = 0
        
#         for i, vi in enumerate(nums):
            
#             for j in range(i+1, n):
                
#                 if i < j and vi <= nums[j]:
                    
#                     curr_w_ramp = j - i
                    
#                     max_w_ramp = max(max_w_ramp, curr_w_ramp)
                    
                    
#         return max_w_ramp
        
        '''
        Approch 2: reduce tc somehow - 2 pointer method
        TC : O(n)
        '''
        
        ans = 0
        n = len(nums)
        
        # array to store max value element on its right side for each index
        right_idx_max = [0 for _ in range(n)]
        right_idx_max[n-1] = nums[n-1] # since last element of array will not have elemen to right side i.e. it is max eleemnt itself
        for i in range(n - 2 , -1 , -1):
            right_idx_max[i] = max(nums[i], right_idx_max[i+1])
        
        left, right = 0, 0 # left contracts range vs right expands range so we need to limit right

        while right < n:
            
            while left < right and nums[left] > right_idx_max[right]:
                left += 1
            
            ans = max(ans, right - left)
            right += 1
        
        return ans