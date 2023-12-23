class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        print(f"nums: {nums}")
        
        moving_sum = nums[0] + nums[1]
        ans = -1
        
        for i in range(2,n):
            if nums[i] < moving_sum:
                ans = max(ans,moving_sum+nums[i])
            moving_sum += nums[i]
            
        return ans