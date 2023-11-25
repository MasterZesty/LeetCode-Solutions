class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans = [0]*n
        
        # approch 1 : TC O(n^2) SC : O(n) ==> TLE
        
        # for i,v in enumerate(nums):
            
            # for j,v in enumerate(nums):
                
                # t = abs( nums[i] - nums[j] )
                
                # ans[i] += t
                
                
                
        # print(ans)
        
        # return ans
        
        # Apoorch 2 :
        
        total_sum = sum(nums)
        
        curr_sum = 0
        
        for i,v in enumerate(nums):
            
            # absDiff = ((number of elements before x1) * x1 - leftSum) +  (rightSum - (number of elements after x1 including x1) * x1);
            
            curr_sum += nums[i]
            
            low_sum = nums[i]*( i + 1 ) - curr_sum
            
            high_sum = ( total_sum - curr_sum ) - ( nums[i]*( n - (i+1) ) )
            
            ans[i] = low_sum + high_sum
        
        
        return ans
        
        
        
        
        
    