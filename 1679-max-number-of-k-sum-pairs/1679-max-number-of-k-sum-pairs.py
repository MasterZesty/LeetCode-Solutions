class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        hm  = {}
        for i,val in enumerate(nums):
            if hm.get(k-val,0) > 0:
                count += 1
                hm[k-val] -= 1
            else:
                hm[val] = hm.get(val,0) + 1

        return count
                
                
                