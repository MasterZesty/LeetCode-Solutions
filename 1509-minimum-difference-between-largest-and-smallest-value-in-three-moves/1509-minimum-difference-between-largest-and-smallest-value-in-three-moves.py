class Solution:
    def minDifference(self, nums: List[int]) -> int:
        '''
        TC - O(nlogn) -- for sorting
        '''
        n = len(nums)
        
        if n <= 4:
            return 0
        
        nums.sort()
        
        '''
        4 possibilities
        delete element from
        
        left| right
        3   |  0
        2   |  1
        1   |  2
        0   |  3
        
        take min of 4 possibilties
        
        '''
        
        return min(nums[-1] - nums[3], nums[-2] - nums[2], nums[-3] - nums[1],  nums[-4] - nums[0] )