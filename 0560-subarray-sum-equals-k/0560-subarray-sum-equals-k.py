class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # hmp_prefix_sum_and_count
        hmp = {}
        sum_ = 0
        count = 0
        
        for i,val in enumerate(nums):
            sum_ += val
            if sum_ == k:
                count += 1
                
            count += hmp.get(sum_ - k,0)
            
            hmp[sum_] = hmp.get(sum_,0) + 1
                
        # print(hmp)
        
        return count
                