class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        
        i = 0
        j = n-1
        mid = n // 2
        
        print(nums)
        nums.sort()
        print(nums)
        
        min_sum = float('-inf')
        
        while i <= mid and j >= mid:
            print(nums[i],nums[j])
            if nums[i] + nums[j] > min_sum:
                min_sum = nums[i] + nums[j]
            i += 1
            j -= 1
            
        return min_sum