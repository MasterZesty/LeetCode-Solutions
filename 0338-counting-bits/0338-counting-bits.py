class Solution:
    def countBits(self, n: int) -> List[int]:
        
        ans = []
        
        for i in range(n+1):
            bin_i = format(i, 'b')
            num_ones = bin_i.count('1')
            # print(f'{i} {bin_i} {num_ones}')
            ans.append(num_ones)
            
            
        return ans