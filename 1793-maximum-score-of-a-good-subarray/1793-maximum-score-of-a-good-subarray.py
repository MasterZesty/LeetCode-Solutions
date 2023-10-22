class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        
        # initialize
        n = len(nums)
        l = k
        r = k
        min_val = nums[k]
        max_score = min_val
        
        # now we expand our window [l.r] until either left reaches to end or right reaches to begining
        while l > 0 or r < n-1:
            # print(f'current window is: {nums[l:r]} ')
            # if next right value is greter than previous left move right 
            if l == 0 or ( r < n - 1 and nums[r+1] > nums[l - 1]  ):
                r += 1
            else:
                # otherwise move left
                l -= 1
                
            # update min val in current window
            min_val = min(min_val, nums[l], nums[r])
                
            # update score
            max_score = max(max_score, min_val*(r - l + 1) )
            
        
        return max_score
            