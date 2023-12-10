class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        row = len(matrix)
        col = len(matrix[0])
        
        ans = [ [ 0 for i in range(row)] for y in range(col)]
        
        # print(f"ans : {ans}")
        
        for i in range(col):
            for j in range(row):
                print(i,j)
                
                ans[i][j] = matrix[j][i]
                
        # print(f"ans : {ans}")
        
        return ans