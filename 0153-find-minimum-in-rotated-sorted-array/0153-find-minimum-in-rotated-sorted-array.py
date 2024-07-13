class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        ref - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/discuss/158940/Beat-100%3A-Very-Simple-(Python)-Very-Detailed-Explanation
        '''
        n = len(nums)
        left = 0
        right = n - 1
        
        while left < right:
            
            mid = (left+right)//2
            
            if nums[mid] > nums[right]: # mid > right
                left = mid + 1
                
            else:
                right = mid
                
        return nums[left]