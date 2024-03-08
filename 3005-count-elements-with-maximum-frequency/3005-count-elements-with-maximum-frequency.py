class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hm = {}
        n = len(nums)
        
        for i in range(n):
            hm[nums[i]] = hm.get(nums[i], 0) + 1
            
        ans = 0
        max_f = max(hm.values())
        # print(hm,max_f)
        
        for num in hm:
            if hm[num] == max_f:
                ans += max_f
                
        return ans