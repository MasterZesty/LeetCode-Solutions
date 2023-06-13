class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # Approch 1 - Success
        # construct cols array
        cols = []
        n = len(grid)
        for x in range(n):
            curr_col = []
            for row in grid:
                curr_col.append(row[x])
            cols.append(curr_col)
            
        #print(f'cols: {cols}')
        
        count = 0
        
        for row in grid:
            for col in cols:
                if row == col:
                    count+= 1
                    #print(f'row: {row} col: {col}')
        
        #print(f'count: {count}')
        
        return count

# Approch 2

# optimized solution does not correctly handle cases where two rows are the 
# same as one column. To address this issue, we can use dictionaries to count
# the occurrences of rows and columns instead of using sets.


#         n = len(grid)
#         count = 0
        
#         # generate tuple of row => {(3, 2, 1), (2, 7, 7), (1, 7, 6)}
#         rows = set(map(tuple, grid))

#         for x in range(n):
#             curr_col = [row[x] for row in grid]
#             if tuple(curr_col) in rows:
#                 count += 1

#         return count

# Approch 3 - Success

#         count = 0
#         n = len(grid)

#         for ri in range(n):
#             for cj in range(n):
#                 if grid[ri] == [row[cj] for row in grid]:
#                     count += 1

#         return count


