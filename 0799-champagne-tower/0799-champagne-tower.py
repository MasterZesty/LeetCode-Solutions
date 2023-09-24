class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        # ref : https://leetcode.com/problems/champagne-tower/discuss/1818207/C%2B%2Bor-Detailed-explanation-w-RECURSION-TO-MEMOZIATION-or-Understand-concept
        
        @cache
        def solve(poured, row, glass):
            
            if row < 0 or glass < 0 or glass > row:
                return 0
            
            if row == 0 and glass == 0:
                return poured
            
            # how much comes from left part- first coordinate(i -1, j - 1) then keep 1 for themself and then divide by 2
            left = ( solve(poured, row - 1, glass -1) - 1 ) / 2
            if left < 0:
                left = 0
            
            # how much comes from right part- first coordinate(i - 1, j) then keep 1 for themself and then divide by 2
            right = ( solve(poured, row - 1, glass) - 1 ) / 2
            if right < 0:
                right = 0
                
            total = left + right
            
            return total
        
        return min(1.0, solve(poured, query_row, query_glass))
            