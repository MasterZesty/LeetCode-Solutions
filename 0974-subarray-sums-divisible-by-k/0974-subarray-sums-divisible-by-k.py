class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """
        Approch 1: brute force method
        TC : O(n^2)
        SC : O(1)
        """
        """
        n = len(nums)
        count = 0
        
        for i in range(n):
            
            for j in range(i,n+1):
                
                if sum(nums[i:j]) % k == 0 and i!=j:
                    # print(i,j,nums[i:j])
                    count += 1
                    
                    
        return count
        """
        """
        ref: 
        
        - 1. https://leetcode.com/problems/subarray-sums-divisible-by-k/discuss/3070694/Thought-Process-to-Reach-the-Solution-oror-C%2B%2B
        - 2. https://leetcode.com/problems/subarray-sums-divisible-by-k/discuss/413234/Whiteboard-explanation."""
        
        hmp = {}
        curr_sum = 0
        count = 0
        
        for i,val in enumerate(nums):
            curr_sum = ( curr_sum +  val%k + k ) % k
            if curr_sum % k == 0:
                count += 1
                
            count += hmp.get(curr_sum,0)
            
            hmp[curr_sum] = hmp.get(curr_sum, 0) + 1
                
        # print(hmp)
        
        return count
        