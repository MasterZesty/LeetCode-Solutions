class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''
        ref: https://leetcode.com/problems/find-peak-element/discuss/4784231/Python-(45ms)-or-Advanced-Binary-Search-or-Easy-to-Understand
        '''
        
        n = len(nums)
        left = 0
        right = n - 1
        
        while left <= right:
            
            mid = (left+right)//2
            
            if mid < n - 1 and nums[mid] < nums[mid+1]:
                # look to right
                left = mid + 1
                
            elif mid > 0 and nums[mid] < nums[mid-1]:
                # look to left
                right = mid - 1
                
            else:
                return mid