class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {}
        
        for index, num in enumerate(nums):
            
            # when num first appears add to dict
            if num not in nums_dict.keys():
                nums_dict[num] = 1
            else:
                nums_dict[num] = nums_dict[num] + 1
                return True
                
        # print(nums_dict.values())
        return False
        