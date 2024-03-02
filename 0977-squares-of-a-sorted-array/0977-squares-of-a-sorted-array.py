class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        '''
        Approach 1: TC - O( n + log n ) SC - O(1)
        '''
        
        n = len(nums)
        
        '''
        for i in range(n):
            nums[i] = nums[i]*nums[i]
            
        
        nums.sort()
            
        return nums
        '''
        
        '''
        Approach 2 : TC - O(log n) SC - O(n)
        '''
        import heapq
        
        sqsort = []
        
        for i in range(n):
            heapq.heappush(sqsort, nums[i]*nums[i])
        
        return [heapq.heappop(sqsort) for i in range(n)]
        