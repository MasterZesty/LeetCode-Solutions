class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        
        if rows == 1 and cols == 1:
            return True
        
        
        for i in range(rows):
            for j in range(cols):
                
                if i+1 < rows and grid[i][j] != grid[i+1][j]:
                    return False
                
                if j+1 < cols and grid[i][j] == grid[i][j+1]:
                    return False
                
        return True