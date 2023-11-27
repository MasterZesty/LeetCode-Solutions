class Solution:
    def knightDialer(self, n: int) -> int:
        
        
        if n == 1:
            return 10
        
        MOD = 10**9 + 7
            
        valid_move = {
            0 : [4,6],
            1 : [8,6],
            2 : [7,9],
            3 : [8,4],
            4 : [0,3,9],
            5 : [],
            6 : [0,1,7],
            7 : [2,6],
            8 : [1,3],
            9 : [4,2]
        }
        
        
        # Initialize a 2D array cur_pos of size n x 10, where n is the length of the phone number and 10 represents the possible digits.
        # Set the values in the first row of dp to 1 because there is only one way to reach each digit from the starting position (the knight is already there).
        
        v = [1] * 10
        # print(f'for n = 1 valid length numbers count are : {v}')
        
        for i in range(2, n+1):
            
            tmp = [0]*10
            
            for key,val in valid_move.items():
                # print(f'compute for cell key : {key} with valid moves val :{val}')
                for j in val:
                    tmp[key] = (tmp[key] + v[j]) % MOD
                    
            
            v = tmp
            
            # print(f'for n = {i} valid length numbers count are : {v}')
        
        return sum(v)%MOD
    
    
        