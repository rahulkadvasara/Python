# 38. Count and Say
# Medium
# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
# countAndSay(1) = "1"
# countAndSay(n) is the run-length encoding of countAndSay(n - 1).
# Run-length encoding (RLE) is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15" and replace "1" with "11". Thus the compressed string becomes "23321511".
# Given a positive integer n, return the nth element of the count-and-say sequence.

# Example 1:
# Input: n = 4
# Output: "1211"
# Explanation:
# countAndSay(1) = "1"
# countAndSay(2) = RLE of "1" = "11"
# countAndSay(3) = RLE of "11" = "21"
# countAndSay(4) = RLE of "21" = "1211"

# Example 2:
# Input: n = 1
# Output: "1"
# Explanation:
# This is the base case.

# Constraints:
# 1 <= n <= 30



# sol 1

# class Solution:
#     def countAndSay(self, n: int) -> str:
#         def process(s):
#             ret = []
#             stack = []
#             for i in s:
#                 if stack and i != stack[-1]:
#                     prev = stack[-1]
#                     count = 0
#                     while stack and stack[-1] == prev:
#                         stack.pop()
#                         count+=1
#                     ret.append(str(count))
#                     ret.append(prev)
#                     stack.append(i)
#                 else:
#                     stack.append(i)
#             if stack:
#                 ret.append(str(len(stack)))
#                 ret.append(stack[-1])
#             return "".join(ret)
#         curr = "1"
#         for i in range(2, n+1):
#             curr = process(curr)
#         return curr
    

# sol 2

# class Solution:
#     def countAndSay(self, n: int) -> str:
#         def count_til_diff(s: str):
#             res = ''
#             i = 0
#             temp = ''
#             while i < len(s):
#                 count = 1
#                 check = s[i]
#                 if (check == temp):
#                     break
#                 temp = check
#                 for j in range(i + 1, len(s)):  
#                     if s[j] != check:
#                         i = j
#                         break
#                     count += 1
#                     if j == len(s) - 1:
#                         i = j
#                         break
#                 res += str(count) + check
#             return res
#         if n == 1:
#             return '1'
#         return count_til_diff(self.countAndSay(n - 1))