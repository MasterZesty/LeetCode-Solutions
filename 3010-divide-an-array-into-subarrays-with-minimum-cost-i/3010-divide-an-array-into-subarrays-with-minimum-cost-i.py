class Solution:
    def minimumCost(self, nums: List[int]) -> int:

        min_cost = nums[0]
        
        t = sorted(nums[1:])
        
        min_cost += t[0] + t[1]
        
        return min_cost
                
            