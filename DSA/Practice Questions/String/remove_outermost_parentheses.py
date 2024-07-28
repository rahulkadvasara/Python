# 1021. Remove Outermost Parentheses

# A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

# For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
# A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

# Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

# Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

 

# Example 1:

# Input: s = "(()())(())"
# Output: "()()()"
# Explanation: 
# The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
# After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
# Example 2:

# Input: s = "(()())(())(()(()))"
# Output: "()()()()(())"
# Explanation: 
# The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
# After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
# Example 3:

# Input: s = "()()"
# Output: ""
# Explanation: 
# The input string is "()()", with primitive decomposition "()" + "()".
# After removing outer parentheses of each part, this is "" + "" = "".
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is either '(' or ')'.
# s is a valid parentheses string.

# sol 1
# class Solution:
#     def removeOuterParentheses(self, s: str) -> str:
#         countB = 0
#         result = ""
#         for i in range(len(s)):
#             if s[i] == '(':
#                 countB += 1
#                 if countB > 1:
#                     result += s[i]
#             elif s[i] == ')':
#                 countB -= 1
#                 if countB > 0:
#                     result += s[i]
#         return result

# sol 2 
# class Solution:
#     def removeOuterParentheses(self, S: str) -> str:
#         res, opened = [], 0
#         for c in S:
#             if c == '(' and opened > 0: res.append(c)
#             if c == ')' and opened > 1: res.append(c)
#             opened += 1 if c == '(' else -1
        
#         return "".join(res)

# sol 3
# class Solution:
#     def removeOuterParentheses(self, S: str) -> str:
#         res, opened = [], 0
#         for c in S:
#             if c == '(' and opened > 0: res.append(c)
#             if c == ')' and opened > 1: res.append(c)
#             opened += 1 if c == '(' else -1
        
#         return "".join(res)

# sol 4
# class Solution:
#     def removeOuterParentheses(self, s: str) -> str:
#         dept = 0
#         result = []

#         for char in s:
#             if char == "(":
#                 if dept > 0:
#                     result.append(char)
#                 dept += 1
#             else:
#                 dept -= 1
#                 if dept > 0:
#                     result.append(char)
#         return "".join(result)
        
            
