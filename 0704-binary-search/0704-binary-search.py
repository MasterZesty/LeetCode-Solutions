class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        i = 0
        j = n - 1
        
        while i <= j:
            
            mid = (i+j)//2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                j = mid - 1
                
            if nums[mid] < target:
                i = mid + 1
        
        return -1