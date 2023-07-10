class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        # approch 1 
        # time complexity - O(n2)
        # space complexity O(1)
        
        n = len(nums)
        ans = 0
        
        for i in range(n):
            
            for j in range(i+1,n):
                
                if abs(nums[i]-nums[j]) == k:
                    # print(nums[i],nums[j])
                    ans += 1
                
        return ans