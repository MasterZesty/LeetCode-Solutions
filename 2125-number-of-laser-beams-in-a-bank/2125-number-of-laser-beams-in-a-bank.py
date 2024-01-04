class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        row = len(bank)
        
        ans = 0
        
        flag = True
        
        for r in range(row):
            
            no_of_lasers = bank[r].count('1')
            # print(f"no_of_lasers : {no_of_lasers} in ith row {r}")
            
            if no_of_lasers != 0:
                
                if flag:
                    prev_no_of_lasers = no_of_lasers
                    flag = False
                    continue
                
                ans += ( prev_no_of_lasers * no_of_lasers )
                prev_no_of_lasers = no_of_lasers
            
        return ans
            