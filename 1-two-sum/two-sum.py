class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i,v in enumerate(nums):
            hm[v] = i

        # print(hm)
        
        for i, n in enumerate(nums):

            b = target - n
            
            if hm.get(b, None) and i != hm.get(b, None):

                return [i, hm.get(target-n)]


        return []