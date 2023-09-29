class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        
        if n <= 1:
            return True
        
        i = 0
        j = 1
        increasing  = True
        decreasing  = True
        
        while j < n:
            
            if i <= j:
                if nums[i] <= nums[j]:
                    # monotone incresing
                    pass
                else:
                    increasing = False
                    
                if nums[i] >= nums[j]:
                    # monotone decreasing
                    pass
                else:
                    decreasing = False
            
            i += 1
            j += 1
            
        
        if not increasing and not decreasing:
            return False
        
        
        return True