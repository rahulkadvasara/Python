
# 11. Container With Most Water
# Medium

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:
# Input: height = [1,1]
# Output: 1
 
# Constraints:
# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104



# sol 1

# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         max_area = 0
#         left = 0
#         right = len(height) - 1
#         while left < right:
#             max_area = max(max_area, (right - left) * min(height[left], height[right]))
#             if height[left] < height[right]:
#                 left += 1
#             else:
#                 right -= 1
#         return max_area



# sol 2

# __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))

# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         x = 0
#         y = len(height) - 1
#         maxv = 0
#         while x<=y:
#             if min(height[x],height[y])*(y-x) > maxv:
#                 maxv = min(height[x],height[y])*(y-x)
#             if height[x] < height[y]:
#                 x+=1
#             else:
#                 y-=1
#         return maxv



# sol 3

# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         left, right = 0, len(height)-1
#         largest_number = max(height)
#         largest = 0
#         while (right-left)*largest_number > largest:
#             area = min(height[left], height[right]) * (right - left)
#             if area > largest:
#                 largest = area
#             if height[left] < height[right]:
#                 left += 1
#             else:
#                 right -= 1
#         return largest