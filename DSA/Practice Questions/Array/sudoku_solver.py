# 37. Sudoku Solver
# Hard

# Write a program to solve a Sudoku puzzle by filling the empty cells.
# A sudoku solution must satisfy all of the following rules:
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.

# Example 1:
# Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
# Explanation: The input board is shown above and the only valid solution is shown below:

# Constraints:
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit or '.'.
# It is guaranteed that the input board has only one solution.

# """
# Do not return anything, modify board in-place instead.
# """



# sol 1

# class Solution:
#     def solveSudoku(self, board: List[List[str]]) -> None:
#         def is_valid(row, col, num):
#             for i in range(9):
#                 if board[row][i] == num or board[i][col] == num or board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
#                     return False
#             return True

#         def solve():
#             for i in range(9):
#                 for j in range(9):
#                     if board[i][j] == '.':
#                         for num in map(str, range(1, 10)):
#                             if is_valid(i, j, num):
#                                 board[i][j] = num
#                                 if solve():
#                                     return True
#                                 board[i][j] = '.'
#                         return False
#             return True

#         solve()



# sol 2

# class Solution:
#     def solveSudoku(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         unsolved = []
#         row = [set() for _ in range(9)]
#         col = [set() for _ in range(9)]
#         square = [set() for _ in range(9)]
        
#         for i in range(9):
#             for j in range(9):
#                 if board[i][j] == ".": 
#                     unsolved.append((i, j))
#                 else: 
#                     row[i].add(board[i][j])
#                     col[j].add(board[i][j])
#                     square[i//3*3+j//3].add(board[i][j])
                    
#         def backtrack(index):
#             if index == len(unsolved): 
#                 return True
            
#             min_candidate = 10
#             min_index = index
#             for x in range(index, len(unsolved)):
#                 i, j = unsolved[x]
#                 box_index = (i // 3) * 3 + (j // 3)
#                 possible = {'1','2','3','4','5','6','7','8','9'} - row[i] - col[j] - square[box_index]
#                 candidates = len(possible)
#                 if candidates < min_candidate:
#                     min_candidate = candidates
#                     min_index = x
#                 if min_candidate == 1:
#                     break 
            
#             unsolved[index], unsolved[min_index] = unsolved[min_index], unsolved[index]
#             i, j = unsolved[index]
#             box_index = (i // 3) * 3 + (j // 3)
#             possible_numbers = {'1','2','3','4','5','6','7','8','9'} - row[i] - col[j] - square[box_index]

#             for num in possible_numbers:
#                 board[i][j] = num
#                 row[i].add(num)
#                 col[j].add(num)
#                 square[i//3*3+j//3].add(num)
#                 if backtrack(index+1): 
#                     return True
#                 row[i].remove(num)
#                 col[j].remove(num)
#                 square[i//3*3+j//3].remove(num)
#                 board[i][j] = '.'
#             return False 
        
#         backtrack(0)



# sol 3.

# class Solution:
#     def solveSudoku(self, board: List[List[str]]) -> None:
#         rowS = defaultdict(set) 
#         colS = defaultdict(set)
#         # {(row_ith_box, col_ith-box): set()}
#         box = defaultdict(set)
#         empty = []
#         # fill existing board
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if board[i][j] != '.':
#                     rowS[i].add(board[i][j])
#                     colS[j].add(board[i][j])
#                     box[(i//3, j//3)].add(board[i][j])
#                 else:
#                     empty.append((i, j))
#         # recursively empty list and fill out empty cell
#         def rec(index):
#             if index == len(empty):
#                 return True
#             i, j = empty[index]
#             for v in range(1, 10):
#                 char = str(v)
#                 if char in rowS[i] or char in colS[j] or char in box[(i//3, j//3)]:
#                     continue
#                 # valid char and updates all hashset,modify board
#                 rowS[i].add(char)
#                 colS[j].add(char)
#                 box[(i//3, j//3)].add(char)
#                 board[i][j] = char
#                 # search next one 
#                 if rec(index+1):
#                     return True
#                 # backtrack reset
#                 rowS[i].remove(char)
#                 colS[j].remove(char)
#                 box[(i//3, j//3)].remove(char)
#                 board[i][j] = "."
#         rec(0)