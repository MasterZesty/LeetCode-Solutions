class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # O(n2) solution
        '''
        for i in range(len(nums)):
            
            for j in range(len(nums)):
                
                if i != j:
                    if nums[i] + nums[j] == target:
                        return [i,j]
                        
        '''
                    
        # O(n) solution
        num_dict = {}
        for i,val in enumerate(nums):
            rem = target - val
            
            if rem in num_dict:
                return [i,num_dict[rem]]
            else:
                num_dict[val] = i
        
               
            
                    
                
            