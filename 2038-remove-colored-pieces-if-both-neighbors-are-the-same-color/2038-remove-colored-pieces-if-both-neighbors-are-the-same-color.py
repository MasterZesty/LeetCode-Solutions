class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        n = len(colors)
        
        if n < 3:
            return False
        
        # suppose a and b are making game moves
        # if a is not having any moves then b winds and vice versa
        #
        # so if we can count how many valid moves a has and b has
        # then we can check who is the winner
        
        a_move_count = 0
        b_move_count = 0
        
        for i in range(1,n-1):
            
            if ( colors[i-1] == 'A' and colors[i] == 'A' and colors[i+1] == 'A' ):
                a_move_count += 1
            
            if ( colors[i-1] == 'B' and colors[i] == 'B' and colors[i+1] == 'B' ):
                b_move_count += 1

                
        return a_move_count > b_move_count