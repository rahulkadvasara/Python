# 1637. Widest Vertical Area Between Two Points Containing No Points

# Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.

# A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.

# Note that points on the edge of a vertical area are not considered included in the area.

 

# Example 1:

# Input: points = [[8,7],[9,9],[7,4],[9,7]]
# Output: 1
# Explanation: Both the red and the blue area are optimal.

# Example 2:

# Input: points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
# Output: 3
 

# Constraints:

# n == points.length
# 2 <= n <= 105
# points[i].length == 2
# 0 <= xi, yi <= 109

# sol 1
# class Solution:
#     def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
#         l=[]
#         for i in range(len(points)):
#             l.append(points[i][0])
#         l.sort()
#         if(len(l)==0 or len(l)==1):
#             return 0
#         c=0
#         for i in range(len(l)-1,0,-1):
#             d=l[i]-l[i-1]
#             if(c<d):
#                 c=d
#         return c

# sol 2
# class Solution:
#     def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:

#         x_cor = [i for i,j in points]

#         x_cor.sort()
#         ans = 0

#         for i in range(len(x_cor)-1):
#             if ans < x_cor[i+1] - x_cor[i]:
#                 ans = x_cor[i+1] - x_cor[i]  
#         return ans

# sol 3
# class Solution:
#     def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
#         xPoints = sorted(set(point[0] for point in points))
#         maxW =0
#         for i in range(1, len(xPoints)):
#             tempMax = xPoints[i] - xPoints[i-1]
#             maxW = max(maxW, tempMax)
#         return maxW

# sol 4
# _f = open('user.out', 'w')
# for points in map(loads, stdin):
#     points = sorted(i[0] for i in points) 
#     print(max((points[i+1]-points[i] for i in range(len(points)-1))), file=_f)
# exit(0)

# sol 3
# class Solution:
#     def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
#         xPoints = sorted(set(point[0] for point in points))
#         maxW =0
#         for i in range(1, len(xPoints)):
#             tempMax = xPoints[i] - xPoints[i-1]
#             maxW = max(maxW, tempMax)
#         return maxW