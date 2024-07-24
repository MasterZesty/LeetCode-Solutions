class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        '''
        TC : nlogn
        '''
        def translate(num):
            digits = list(str(num))
            
            for d in range(len(digits)):
                digits[d] = str(mapping[int(digits[d])])
                
            return int("".join(digits))
        
        num_map = {}
        
        for num in nums:
            num_map[num] = translate(num)
            
        nums.sort(key=lambda val: num_map[val])
        
        return nums