# 69. Sqrt(x)
# Easy

# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

# Example 1:

# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.
# Example 2:

# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 

# Constraints:

# 0 <= x <= 231 - 1



# sol 1

# class Solution:
#     def mySqrt(self, x: int) -> int:
#         return int(x ** 0.5)


# sol 2

# class Solution:
#     def mySqrt(self, x: int) -> int:
#         if x == 0:
#             return 0
#         first, last = 1, x
#         while first <= last:
#             mid = first + (last - first) // 2
#             if mid == x // mid:
#                 return mid
#             elif mid > x // mid:
#                 last = mid - 1
#             else:
#                 first = mid + 1
#         return last