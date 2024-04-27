class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        
        if row < 2 or col < 2:
            return 0
            
        
        num_1_row = [0 for _ in range(row)]
        num_1_col = [0 for _ in range(col)]
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    num_1_row[i] += 1
                    num_1_col[j] += 1
            
        # print(f"num_1_row: {num_1_row} | num_1_col: {num_1_col}")
        
        ans = 0
        
        for i in range(row):
            if num_1_row[i] > 1:
                for j in range(col):
                    if grid[i][j] == 1:
                        if num_1_col[j] > 1:
                            m = num_1_row[i] - 1
                            n = num_1_col[j] - 1
                            t = m*n
                            ans += t
                        
                        
        return ans