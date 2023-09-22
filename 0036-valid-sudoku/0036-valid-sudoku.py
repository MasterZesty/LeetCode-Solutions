class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # validate row
        for row in board:
            dot_count = row.count(".")
            unique_num_count = len(row) if dot_count == 0 else len(set(row)) - 1
            
            if unique_num_count != len(row) - dot_count:
                # print(f'row validation failed')
                return False
            
        #validate cols
        t_board = list(map(list, zip(*board)))
        # print(t_board)
        for col in t_board:
            dot_count = col.count(".")
            unique_num_count = len(col) if dot_count == 0 else len(set(col)) - 1
            
            if unique_num_count != len(col) - dot_count:
                # print(f'col validation fialed')
                return False
            
        # validate box
        for i in range(0,len(board),3):
            for j in range(0,len(board[i]),3):
                # print(board[i][j:j+3])
                # print(board[i+1][j:j+3])
                # print(board[i+2][j:j+3])
                
                t = board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3]
                dot_count = t.count(".")
                unique_num_count = len(t) if dot_count == 0 else len(set(t)) - 1

                if unique_num_count != len(t) - dot_count:
                    # print(f'box validation failed')
                    return False
        
        return True