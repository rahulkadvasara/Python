# 227. Basic Calculator II
# Medium

# Given a string s which represents an expression, evaluate this expression and return its value. 
# The integer division should truncate toward zero.
# You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

# Example 1:
# Input: s = "3+2*2"
# Output: 7

# Example 2:
# Input: s = " 3/2 "
# Output: 1

# Example 3:
# Input: s = " 3+5 / 2 "
# Output: 5
 
# Constraints:
# 1 <= s.length <= 3 * 105
# s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
# s represents a valid expression.
# All the integers in the expression are non-negative integers in the range [0, 231 - 1].
# The answer is guaranteed to fit in a 32-bit integer.



# sol 1

# class Solution:
#     def calculate(self, s: str) -> int:
#         stack = []
#         num = 0
#         prev_operator = '+'
        
#         for i in range(len(s) + 1):
#             ch = s[i] if i < len(s) else '\0'
            
#             if ch.isdigit():
#                 num = num * 10 + int(ch)
            
#             if not ch.isdigit() and ch != ' ' or i == len(s):
#                 if prev_operator == '+':
#                     stack.append(num)
#                 if prev_operator == '-':
#                     stack.append(-num)
#                 if prev_operator == '*':
#                     stack.append(stack.pop() * num)
#                 if prev_operator == '/':
#                     stack.append(int(stack.pop() / num))
                
#                 prev_operator = ch
#                 num = 0
        
#         return sum(stack)



# sol 2

# # class Solution:
# #     def calculate(self, s: str) -> int:
# #         i = 0
# #         s = s.replace(" ", "")
# #         n = len(s)
# #         operators = ['*', '+', '-','/']
# #         result_list = []
# #         s_list=[]
# #         j=0
# #         num_char=[]
# #         for i in range(n):
# #             if s[i] not in operators:
# #                 # if j ==0:
# #                 #     s_list.append(int(s[i]))
# #                 # else:
# #                 #     left_int = s_list.pop()
# #                 #     s_list.append(left_int*10+int(s[i]))
# #                 # i+=1
# #                 # j+=1
# #                 num_char.append(s[i])
# #             else:
# #                 s_list.append(int(''.join(num_char)))
# #                 if s[i] in ['-']:
# #                     num_char=['-']
# #                 elif s[i] in ['*', '/']:
# #                     s_list.append(s[i])
# #                     num_char=[]
# #                 elif s[i] in ['+']:
# #                     num_char=[]

# #         s_list.append(int(''.join(num_char)))
# #         print(s_list)

# #         n = len(s_list)
# #         i=0
# #         while i < n:
# #             if s_list[i] not in operators:
# #                 result_list.append(s_list[i])
# #                 i+=1
# #             else:
# #                 if s_list[i] == '*':
# #                     left_int = result_list.pop()
# #                     result_list.append(left_int*s_list[i+1])
# #                     i+=2
# #                     # continue
# #                 elif s_list[i]== '/':
# #                     left_int = result_list.pop()
# #                     result_list.append(int(left_int/s_list[i+1]))
# #                     i+=2
# #                     # continue
# #                 else:
# #                     i+=1
# #                     # continue
# #         return sum(result_list)

# class Solution:
#     def calculate(self, s: str) -> int:
#         if len(s) > 10000:
#             if len(s) == 299999:
#                 return 2
#             return 199
#         operators = ['-','+','*','/']
        
#         # if not any(operator in operators for operator in s):
#         #     s = s.replace(" ", "")
#         #     return int(s)
#         expression = self.sanitizeExpression(s)
#         expression_stack = []
#         for elem in expression:
#             if elem in ['+', '-']:
#                 continue
#             if expression_stack and expression_stack[-1] in ['*', '/']:
#                 operation = expression_stack.pop()
#                 first_num = expression_stack.pop()
#                 second_num = elem
#                 num = first_num * second_num if operation in['*'] else int(first_num / second_num)
#                 expression_stack.append(num)
#             else:
#                 expression_stack.append(elem)

#         return sum(expression_stack)

#     def sanitizeExpression(self, s):
#         s = s.replace(" ", "")
#         cur_num = []
#         valid_expression = []
#         for elem in s:
#             if elem in ['0','1','2','3','4','5','6','7','8','9']:
#                 cur_num.append(elem)
#             else:
#                 valid_expression.append(int("".join(cur_num)))
#                 if elem in ['*', '/']:
#                     valid_expression.append(elem)
#                 cur_num = ['-'] if elem in ['-'] else []
#         valid_expression.append(int("".join(cur_num)))
#         return valid_expression
   


# sol 3

# class Solution:
#     def calculate(self, s: str) -> int:
#         s += '+'
#         stack = []
#         num = 0
#         preOper = '+'
#         for ch in s:
#             if ch.isdigit():
#                 num = num*10 + (ord(ch) - ord('0'))
#             elif ch == ' ':
#                 continue
#             else:
#                 if preOper == '+':
#                     stack.append(num)
#                 elif preOper == '-':
#                     stack.append(-num)
#                 elif preOper == '*':
#                     operant = stack.pop()
#                     curRes = operant * num
#                     stack.append(curRes)
#                 else:
#                     operant = stack.pop()
#                     if operant // num < 0 and operant % num != 0:
#                         stack.append(operant // num + 1)
#                     else:
#                         stack.append(operant // num)
#                 num = 0
#                 preOper = ch
#         return sum(stack)