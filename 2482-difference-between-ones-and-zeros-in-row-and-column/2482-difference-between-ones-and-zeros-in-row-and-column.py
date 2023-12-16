class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        
        rows = len(grid)
        cols = len(grid[0])
        
        onesRow = [0]*rows
        zerosRow = [0]*rows
        
        onesCol = [0]*cols
        zerosCol = [0]*cols
        
        for i in range(rows):
            for j in range(cols):
                # print(f"i: {i} j: {j} | grid: {grid[i][j]}")
                
                if grid[i][j] == 1:
                    onesRow[i] += 1
                    onesCol[j] += 1
                
                if grid[i][j] == 0:
                    zerosRow[i] += 1
                    zerosCol[j] += 1
                    
        # print(f"onesRow: {onesRow}")
        # print(f"zerosRow: {zerosRow}")
        # print(f"onesCol: {onesCol}")
        # print(f"zeroscol: {zerosCol}")
        
        
        for i in range(rows):
            for j in range(cols):
                grid[i][j] = onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j]
        
        
        return grid

                    
                