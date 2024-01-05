class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        '''
        nlog ref:https://leetcode.com/problems/longest-increasing-subsequence/discuss/4509303/Beats-100-Binary-Search-Explained-with-Video-C%2B%2BJavaPythonJS
        '''
        n = len(nums)
        long_incr_subseq = [0]*n
        size = 0
        
        for num in nums:
            i = 0
            j = size
            while i != j:
                
                mid = (i+j)//2
                
                if long_incr_subseq[mid] < num:
                    i = mid + 1
                    
                else:
                    j = mid
                    
            long_incr_subseq[i] = num
            
            size = max( size, i + 1 )
            
            
        return size
        