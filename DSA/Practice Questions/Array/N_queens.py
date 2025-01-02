# 51. N-Queens
# Hard

# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

# Example 1:
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

# Example 2:
# Input: n = 1
# Output: [["Q"]]
 
# Constraints:
# 1 <= n <= 9


# sol 1

# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         def is_not_under_attack(row, col):
#             return not (cols[col] or hill_diagonals[row - col] or dale_diagonals[row + col])
        
#         def place_queen(row, col):
#             queens.add((row, col))
#             cols[col] = 1
#             hill_diagonals[row - col] = 1
#             dale_diagonals[row + col] = 1
        
#         def remove_queen(row, col):
#             queens.remove((row, col))
#             cols[col] = 0
#             hill_diagonals[row - col] = 0
#             dale_diagonals[row + col] = 0
        
#         def add_solution():
#             solution = []
#             for _, col in sorted(queens):
#                 solution.append('.' * col + 'Q' + '.' * (n - col - 1))
#             output.append(solution)
        
#         def backtrack(row):
#             for col in range(n):
#                 if is_not_under_attack(row, col):
#                     place_queen(row, col)
#                     if row + 1 == n:
#                         add_solution()
#                     else:
#                         backtrack(row + 1)
#                     remove_queen(row, col)
        
#         cols = [0] * n
#         hill_diagonals = [0] * (2 * n - 1)
#         dale_diagonals = [0] * (2 * n - 1)
#         queens = set()
#         output = []
#         backtrack(0)
#         return output



# sol 2

# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         row = set()
#         col = set()
#         diag1 = set()  # Tracks i - j
#         diag2 = set()  # Tracks i + j

#         def dfs(r):
#             if r == n:
#                 ans.append([''.join(row) for row in tmp])
#                 return
#             for c in range(n):
#                 if c in col or (r - c) in diag1 or (r + c) in diag2:
#                     continue
#                 tmp[r][c] = 'Q'
#                 col.add(c)
#                 diag1.add(r - c)
#                 diag2.add(r + c)
#                 dfs(r + 1)
#                 tmp[r][c] = '.'
#                 col.remove(c)
#                 diag1.remove(r - c)
#                 diag2.remove(r + c)

#         ans = []
#         tmp = [['.'] * n for _ in range(n)]
#         dfs(0)
#         return ans