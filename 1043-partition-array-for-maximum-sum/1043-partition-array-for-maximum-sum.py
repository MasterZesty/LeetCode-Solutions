class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        '''
        Approch 1: recursion TLE
        Approch 2 : dp
        '''
        
        n = len(arr)
        
        dp = [-1 for d in range(n)]


        def solve(arr, k, dp, i):
            
            if i >= n:
                return 0
            
            if dp[i] != -1:
                return dp[i]
            
            maxval = 0
            ans = 0
            
            for j in range(i, min(n,i+k) ):
                maxval = max(maxval, arr[j])
                ans = max(ans, (j-i+1)*maxval + solve(arr, k, dp, j+1))
                
            dp[i] = ans
                
            return ans

        
        return solve(arr, k, dp, 0)