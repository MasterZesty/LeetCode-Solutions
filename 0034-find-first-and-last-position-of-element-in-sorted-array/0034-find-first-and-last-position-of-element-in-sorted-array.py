class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        from bisect import bisect_left, bisect_right
        
        lo = 0
        hi = len(nums)
        
        if lo == 0 and hi == 0:
            return [-1, -1]
        
        pos_i = bisect_left(nums, target, lo, hi)
        i = pos_i if pos_i != hi and nums[pos_i] == target else -1
        
        pos_j = bisect_right(nums, target, lo, hi)
        print(pos_j)
        j = pos_j - 1 if pos_j-1 != hi and nums[pos_j-1] == target else -1
        
        # print(i,j)
        
        
        return [i,j]