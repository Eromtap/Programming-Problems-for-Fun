'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.



'''


class Solution(object):
    def isValidSudoku(self, board):
        for i in board:
            digits = []
            for j in i:
                if j == '.':
                    continue
                else:
                    if j not in digits:
                        digits.append(j)
                    else:
                        return False
        for i in range(len(board)):
            count = 0
            digits = []
            for j in range(len(board)):
                    if board[count][i] == '.':
                        count += 1
                    else:
                        if board[count][i] not in digits:
                            digits.append(board[count][i])
                            count += 1
                        else:
                            return False    
     
        def square(row, column):
            square = []
            for i in range(row, row + 3):
                
                for j in range(3):
                    if board[i][j+column] == '.':
                        continue
                    if board[i][j+column] not in square:
                        square.append(board[i][j+column])
                    else:
                        return False

            return True
            
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not square(j, i):
                    return False
        return True
        
    

        






board = [
     ["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]



# board = [
#     ["8","3",".",".","7",".",".",".","."]
#     ,["6",".",".","1","9","5",".",".","."]
#     ,[".","9","8",".",".",".",".","6","."]
#     ,["8",".",".",".","6",".",".",".","3"]
#     ,["4",".",".","8",".","3",".",".","1"]
#     ,["7",".",".",".","2",".",".",".","6"]
#     ,[".","6",".",".",".",".","2","8","."]
#     ,[".",".",".","4","1","9",".",".","5"]
#     ,[".",".",".",".","8",".",".","7","9"]]





x = Solution()
print(x.isValidSudoku(board))
