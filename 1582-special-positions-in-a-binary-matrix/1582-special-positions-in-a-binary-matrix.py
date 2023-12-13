class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        
        n = len(mat)
        m = len(mat[0])
        
        row_count = [0]*n
        col_count = [0]*m
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    
                    row_count[i] += 1
                    col_count[j] += 1
                    
        # print(row_count)
        # print(col_count)
        
        count = 0
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    if row_count[i] == 1 and col_count[j] == 1:
                        count += 1
                    
        return count