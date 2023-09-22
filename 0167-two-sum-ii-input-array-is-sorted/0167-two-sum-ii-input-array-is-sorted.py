class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_hmap = {}
        for index,num in enumerate(numbers):

            if (target - num) in num_hmap:
                # print(f'idx {index} oidx {num_hmap[target-num]}')
                return sorted([index+1, num_hmap[target-num]+1])
            
            num_hmap[num] = index
                
        return []