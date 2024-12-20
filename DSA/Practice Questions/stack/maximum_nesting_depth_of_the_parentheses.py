# 1614. Maximum Nesting Depth of the Parentheses
# Easy

# Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.

# Example 1:
# Input: s = "(1+(2*3)+((8)/4))+1"
# Output: 3
# Explanation:
# Digit 8 is inside of 3 nested parentheses in the string.

# Example 2:
# Input: s = "(1)+((2))+(((3)))"
# Output: 3
# Explanation:
# Digit 3 is inside of 3 nested parentheses in the string.

# Example 3:
# Input: s = "()(())((()()))"
# Output: 3

# Constraints:
# 1 <= s.length <= 100
# s consists of digits 0-9 and characters '+', '-', '*', '/', '(', and ')'.
# It is guaranteed that parentheses expression s is a VPS.



# sol 1

# class Solution:
#     def maxDepth(self, s):
#         count = 0
#         max_num = 0
#         for i in s:
#             if i == "(":
#                 count += 1
#                 if max_num < count:
#                     max_num = count
#             if i == ")":
#                 count -= 1
#         return(max_num)



# sol 2

# class Solution:
#     def maxDepth(self, s: str) -> int:
#         count = 0
#         max_depth = 0
#         for char in s:
#             if char == '(':
#                 count += 1
#             max_depth = max(count, max_depth)
#             if char == ')':
#                 count -= 1
#         return max_depth
    


# sol 3

# class Solution:
#     def maxDepth(self, s: str) -> int:
#         ans, p=0, 0
#         for c in s:
#             p+=(c=='(')-(c==')')
#             ans=max(ans, p)
#         return ans


# sol 4

# class Solution:
#     def maxDepth(self, s: str) -> int:
#         stack = []
#         depth = 0
#         for ch in s:
#             if ch == '(':
#                 stack.append(ch)
#             elif ch == ')':
#                 depth = max(depth, len(stack))
#                 stack.pop()
#         return depth
    



