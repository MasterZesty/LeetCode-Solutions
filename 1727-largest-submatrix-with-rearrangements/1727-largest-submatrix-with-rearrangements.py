class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        
        rows = len(matrix)
        columns = len(matrix[0])
        
        max_area = 0
        
        # find max height possibel for each column
        for row in range(rows):
            
            for col in range(columns):
                
                if matrix[row][col] != 0 and row>0:
                    # add height
                    matrix[row][col] += matrix[row-1][col]         
                
                    
        # print(f'height matrix {matrix}')
        
        
        for row in range(rows-1,-1,-1):
            
            matrix[row].sort()

            k = 1
            
            for col in range(columns-1,-1,-1):
                
                # print(row,col)

                max_area = max( max_area, matrix[row][col]*k)
                
                k += 1
                
                
                
                
                
        return max_area