class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        '''
        Approach 1: TC - O( nlog n ) SC - O(1)
        '''
        
        n = len(nums)
        
        '''
        for i in range(n):
            nums[i] = nums[i]*nums[i]
            
        
        nums.sort()
            
        return nums
        '''
        
        '''
        Approach 2 : TC - O(nlog n) SC - O(n)
        '''
        '''
        import heapq
        
        sqsort = []
        
        for i in range(n):
            heapq.heappush(sqsort, nums[i]*nums[i])
        
        return [heapq.heappop(sqsort) for i in range(n)]
        '''
        
        '''
        Approach 3 : two pointer method
        '''
        l = 0
        r = n - 1
        i = n - 1
        ans = [0]*n
        
        while l <= r:
            l_sq = nums[l]*nums[l]
            r_sq = nums[r]*nums[r]
            
            if l_sq >= r_sq:
                ans[i] = l_sq
                l += 1
            else:
                ans[i] = r_sq
                r -= 1
            
            i -= 1
        
        return ans
        
        
        
        
        
        
        