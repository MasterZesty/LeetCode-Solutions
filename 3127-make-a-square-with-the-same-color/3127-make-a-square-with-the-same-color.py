class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        
        # will use moving window to check each 2x2
        
        n = len(grid)
        
        i = 0
        
        while i <= n - 2:
            
            j = 0
            
            while j <= n - 2:
                
                # check if black is possible
                is_black = 0
                
                if grid[i][j] == "B":
                    is_black += 1
                
                if grid[i][j+1] == "B":
                    is_black += 1
                    
                if grid[i+1][j] == "B":
                    is_black += 1
                    
                if grid[i+1][j+1] == "B":
                    is_black += 1
                    
                if is_black == 0 or is_black == 1 or is_black == 3 or is_black==4:
                    return True
                
                j += 1
            
            i += 1
            
        return False