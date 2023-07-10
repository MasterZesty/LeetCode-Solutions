class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        # approch one O(n2)
        
        n = len(nums)
        ans = 0
        
        for i in range(n):
            
            for j in range(i+1,n):
                
                if abs(nums[i]-nums[j]) == k:
                    print(nums[i],nums[j])
                    ans += 1
                
        return ans