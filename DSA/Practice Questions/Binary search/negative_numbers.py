# 1351. Count Negative Numbers in a Sorted Matrix

# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.
 
# Example 1:

# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.
# Example 2:

# Input: grid = [[3,2],[1,0]]
# Output: 0
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# -100 <= grid[i][j] <= 100
 

# Follow up: Could you find an O(n + m) solution?


# sol 1
# Linear search
# O(n^2)
# class Solution:
#     def countNegatives(self, grid: List[List[int]]) -> int:
#         op=0
#         for i in range(len(grid)):
#             for j in range(len(grid[i])):
#                 if grid[i][j]<0:
#                     op+=1
#         return op

# sol 2
# class Solution:
#     def countNegatives(self, grid: List[List[int]]) -> int:

#         bin = lambda y: bisect_right(y, .5, key = lambda x: -x)
#         return len(grid)*len(grid[0])- sum(map(bin, grid))

# sol 3
# binary search
# O(m+n)
# class Solution:
#     def countNegatives(self, grid: List[List[int]]) -> int:
#         n = len(grid)
#         x, i = 0, len(grid[0])-1
#         total = 0

#         while i >= 0 and x < n:
#             if grid[x][i] < 0:
#                 total += n - x
#                 i -= 1
#             else:
#                 x += 1
#         return total

# sol 4
# binary search
# O(m+n)
# class Solution:
#     def countNegatives(self, grid: List[List[int]]) -> int:
#         ROWS, COLS = len(grid), len(grid[0])
#         negatives = 0
#         col = 0
#         for row in range(ROWS - 1, -1, -1):
#             while col < COLS and grid[row][col] >= 0:
#                 col += 1
#             negatives += COLS - col
#         return negatives

# # sol 5
# # import numpy as np
# # class Solution:
# #     def countNegatives(self, grid: List[List[int]]) -> int:
# #         # count = 0
# #         arr = np.array(grid)
# #         # for l_0 in grid:
# #         #     for i in l_0:
# #         #         # for i in l_1:
# #         #         if i < 0:
# #         #             count += 1
# #         count = np.sum(arr < 0)
        
# #         return count

# def countNegatives(grid: List[List[int]]) -> int:
#     c=0
#     for i in grid:
#         for j in i:
#             if j < 0:
#                 c+=1
#     return c
# f = open("user.out","w") 
# a = 0
# for case in map(loads, stdin):
#     for i in range(2):
#         if a==0:
#             b = case
#             a += 1
#         else:
#             print(str(countNegatives(b)), file = f)
#             a = a - 1
# exit(0)

