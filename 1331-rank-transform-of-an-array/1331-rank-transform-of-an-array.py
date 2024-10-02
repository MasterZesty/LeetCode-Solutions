class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        sorted_arr = sorted(arr)
        
        number_rank_dict = {}
        
        for idx, num in enumerate(sorted_arr):
            if number_rank_dict.get(num, 0) == 0:
                number_rank_dict[num] = len(number_rank_dict) + 1
            
        # print(number_rank_dict)
        
        return [number_rank_dict[n] for n in arr]
        