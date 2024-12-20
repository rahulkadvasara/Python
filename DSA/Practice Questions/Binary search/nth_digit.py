# 400. Nth Digit
# Medium

# Given an integer n, return the nth digit of the infinite integer sequence [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...].

# Example 1:
# Input: n = 3
# Output: 3

# Example 2:
# Input: n = 11
# Output: 0
# Explanation: The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.

# Constraints:
# 1 <= n <= 231 - 1



# sol 1

# class Solution:
#     def findNthDigit(self, n: int) -> int:
#         digit_in_num = 1
#         start = 1
#         end = 9
#         while n > digit_in_num * end:
#             n -= digit_in_num * end
#             digit_in_num += 1
#             start *= 10
#             end *= 10
#         num = start + (n - 1) // digit_in_num
#         return int(str(num)[(n - 1) % digit_in_num])
    


# sol 2

# class Solution:
#     def findNthDigit(self, n: int) -> int:
#         digit = base = 1
#         while n > 9*base*digit:
#             n -= 9*base*digit
#             digit += 1
#             base *= 10 
#         q, r = divmod(n-1, digit)
#         return int(str(base + q)[r])