class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        row = len(bank)
        
        laser = []
        
        ans = 0
        
        for r in range(row):
            
            no_of_lasers = sum( map(int,list(bank[r]) ) )
            # print(f"no_of_lasers : {no_of_lasers} in ith row {r}")
            
            if no_of_lasers != 0:
                laser.append(no_of_lasers)
                
                if len(laser) < 2:
                    prev_no_of_lasers = no_of_lasers
                    continue
                
                ans += ( prev_no_of_lasers * no_of_lasers )
                prev_no_of_lasers = no_of_lasers
            
        return ans
            