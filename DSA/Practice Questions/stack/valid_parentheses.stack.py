# 20. Valid Parentheses
# Easy

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([])"
# Output: true

# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.



# # sol 1

# class Solution(object):
#     def isValid(self, s):
#         # Create a pair of opening and closing parrenthesis...
#         opcl = dict(('()', '[]', '{}'))
#         # Create stack data structure...
#         stack = []
#         # Traverse each charater in input string...
#         for idx in s:
#             # If open parentheses are present, append it to stack...
#             if idx in '([{':
#                 stack.append(idx)
#             # If the character is closing parentheses, check that the same type opening parentheses is being pushed to the stack or not...
#             # If not, we need to return false...
#             elif len(stack) == 0 or idx != opcl[stack.pop()]:
#                 return False
#         # At last, we check if the stack is empty or not...
#         # If the stack is empty it means every opened parenthesis is being closed and we can return true, otherwise we return false...
#         return len(stack) == 0


# # sol 2

# class Solution:
#     def isValid(self, s: str) -> bool:
#         open_braces = ["(", "[", "{"]
#         close_braces = [")", "]", "}"]
#         stack = []

#         for c in s:
#             if c in open_braces:
#                 stack.append(c)
#             elif c in close_braces:
#                 if len(stack) == 0:
#                     return False

#                 prev_open = stack[-1]
#                 prev_open_idx = open_braces.index(prev_open)
#                 close_idx = close_braces.index(c)

#                 if prev_open_idx == close_idx:
#                     stack.pop(-1)
#                 else:
#                     return False
#         return len(stack) == 0