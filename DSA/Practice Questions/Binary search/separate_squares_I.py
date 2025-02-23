# 3453. Separate Squares I
# Medium

# You are given a 2D integer array squares. Each squares[i] = [xi, yi, li] represents the coordinates of the bottom-left point and the side length of a square parallel to the x-axis.
# Find the minimum y-coordinate value of a horizontal line such that the total area of the squares above the line equals the total area of the squares below the line.
# Answers within 10-5 of the actual answer will be accepted.
# Note: Squares may overlap. Overlapping areas should be counted multiple times.
 
# Example 1:
# Input: squares = [[0,0,1],[2,2,1]]
# Output: 1.00000
# Explanation:
# Any horizontal line between y = 1 and y = 2 will have 1 square unit above it and 1 square unit below it. The lowest option is 1.

# Example 2:
# Input: squares = [[0,0,2],[1,1,1]]
# Output: 1.16667
# Explanation:
# The areas are:
# Below the line: 7/6 * 2 (Red) + 1/6 (Blue) = 15/6 = 2.5.
# Above the line: 5/6 * 2 (Red) + 5/6 (Blue) = 15/6 = 2.5.
# Since the areas above and below the line are equal, the output is 7/6 = 1.16667.

# Constraints:
# 1 <= squares.length <= 5 * 104
# squares[i] = [xi, yi, li]
# squares[i].length == 3
# 0 <= xi, yi <= 109
# 1 <= li <= 109
# The total area of all the squares will not exceed 1012.



# sol 1

# class Solution:
#     def separateSquares(self, squares: List[List[int]]) -> float:
#         def helper(line: float, squares: List[List[int]]) -> float:
#             aAbove = 0.0
#             aBelow = 0.0
#             for sq in squares:
#                 x, y, l = sq
#                 total = l * l
#                 if line <= y:
#                     aAbove += total
#                 elif line >= y + l:
#                     aBelow += total
#                 else:
#                     # The line intersects the square.
#                     aboveHeight = (y + l) - line
#                     belowHeight = line - y
#                     aAbove += l * aboveHeight
#                     aBelow += l * belowHeight
#             return aAbove - aBelow
#         lo = 0
#         hi = 2*1e9
#         for sq in squares:
#             y, l = sq[1], sq[2]
#             lo = min(lo, float(y))
#             hi = max(hi, float(y) + l)
#         for _ in range(60):
#             mid = (lo + hi) / 2.0
#             diff = helper(mid, squares)
#             if diff > 0:
#                 lo = mid
#             else:
#                 hi = mid
        
#         return hi



# sol 2

# class Solution:
#     def separateSquares(self, squares: List[List[int]]) -> float:
#         # dic = defaultdict(int) # dic[i] = total area between y = i-1 and y = i
#         deldic = {} # dic[i+1] - dic[i]
#         totalA = 0
#         for x, y, l in squares:
#             if y in deldic:
#                 deldic[y] += l
#             else:
#                 deldic[y] = l
#             if y+l in deldic:
#                 deldic[y+l] -= l
#             else:
#                 deldic[y+l] = -l
#             totalA += l ** 2
#         halfA = totalA / 2
#         currentA = 0
#         to_try = sorted(deldic.keys())
#         currentD = 0
#         length = len(to_try)
#         for i in range(length - 1):
#             y = to_try[i]
#             currentD += deldic[y]
#             currentA += (to_try[i+1] - to_try[i]) * currentD
#             if currentA >= halfA:
#                 y = to_try[i+1] - (currentA - halfA) / currentD
#                 break
#         return y

#         #[[522261215,954313664,461744743],[628661372,718610752,21844764],[619734768,941310679,91724451],[352367502,656774918,591943726],[860247066,905800565,853111524],[817098516,868361139,817623995],[580894327,654069233,691552059],[182377086,256660052,911357],[151104008,908768329,890809906],[983970552,992192635,462847045]]
                