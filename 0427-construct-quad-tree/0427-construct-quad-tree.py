"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
        def construct(self, grid: List[List[int]]) -> 'Node':
            n = len(grid)
            return(self.constructHelper(grid, 0, 0, n-1, n-1))
        
        
        def constructHelper(self, grid, rowStart, colStart, rowEnd, colEnd):
            
            if rowStart > rowEnd or colStart > colEnd:
                return None
            isLeaf = True
            val = grid[rowStart][colStart]
            for i in range(rowStart, rowEnd+1):
                for j in range(colStart, colEnd+1):
                    if grid[i][j] != val:
                        isLeaf = False
                        break
                if not isLeaf:
                    break
                        
            if isLeaf:
                return Node(val == 1, True, None, None, None, None)
            rowMid = (rowStart + rowEnd) // 2
            colMid = (colStart + colEnd) // 2
            topLeft = self.constructHelper(grid, rowStart, colStart, rowMid, colMid)
            topRight = self.constructHelper(grid, rowStart, colMid+1, rowMid, colEnd)
            bottomLeft = self.constructHelper(grid, rowMid+1, colStart, rowEnd, colMid)
            bottomRight = self.constructHelper(grid, rowMid+1, colMid+1, rowEnd, colEnd)
            return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)
        
#         # code start here
        
        
#     def construct(self, grid: List[List[int]]) -> 'Node':
#         return self.constructHelper(grid, 0, 0, len(grid)-1, len(grid[0])-1)
    
#     def constructHelper(self, grid, rowStart, colStart, rowEnd, colEnd):
#         if rowStart > rowEnd or colStart > colEnd:
#             return None
#         isLeaf = True
#         val = grid[rowStart][colStart]
#         for i in range(rowStart, rowEnd+1):
#             for j in range(colStart, colEnd+1):
#                 if grid[i][j] != val:
#                     isLeaf = False
#                     break
#             if not isLeaf:
#                 break
#         if isLeaf:
#             return Node(val == 1, True, None, None, None, None)
#         rowMid = (rowStart + rowEnd) // 2
#         colMid = (colStart + colEnd) // 2
#         topLeft = self.constructHelper(grid, rowStart, colStart, rowMid, colMid)
#         topRight = self.constructHelper(grid, rowStart, colMid+1, rowMid, colEnd)
#         bottomLeft = self.constructHelper(grid, rowMid+1, colStart, rowEnd, colMid)
#         bottomRight = self.constructHelper(grid, rowMid+1, colMid+1, rowEnd, colEnd)
#         return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)
        
       