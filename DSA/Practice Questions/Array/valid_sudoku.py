# 36. Valid Sudoku
# Medium

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

# Example 1:
# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

# Example 2:
# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

# Constraints:
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.



# sol 1

# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         seen = set()
#         for i in range(9):
#             for j in range(9):
#                 if board[i][j] != '.':
#                     if (i, board[i][j]) in seen or (board[i][j], j) in seen or (i//3, j//3, board[i][j]) in seen:
#                         return False
#                     seen.add((i, board[i][j]))
#                     seen.add((board[i][j], j))
#                     seen.add((i//3, j//3, board[i][j]))
#         return True
    


# sol 2

# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         rows = [{} for _ in range(9)]
#         cols = [{} for _ in range(9)]
#         boxes = [{} for _ in range(9)]
        
#         for i in range(9):
#             for j in range(9):
#                 num = board[i][j]
#                 if num != '.':
#                     box_index = (i // 3) * 3 + j // 3
                    
#                     rows[i][num] = rows[i].get(num, 0) + 1
#                     cols[j][num] = cols[j].get(num, 0) + 1
#                     boxes[box_index][num] = boxes[box_index].get(num, 0) + 1
                    
#                     if rows[i][num] > 1 or cols[j][num] > 1 or boxes[box_index][num] > 1:
#                         return False
#         return True