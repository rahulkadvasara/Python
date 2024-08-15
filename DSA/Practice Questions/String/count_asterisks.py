# 2315. Count Asterisks
# Easy
# Topics
# Companies
# Hint
# You are given a string s, where every two consecutive vertical bars '|' are grouped into a pair. In other words, the 1st and 2nd '|' make a pair, the 3rd and 4th '|' make a pair, and so forth.

# Return the number of '*' in s, excluding the '*' between each pair of '|'.

# Note that each '|' will belong to exactly one pair.

 

# Example 1:

# Input: s = "l|*e*et|c**o|*de|"
# Output: 2
# Explanation: The considered characters are underlined: "l|*e*et|c**o|*de|".
# The characters between the first and second '|' are excluded from the answer.
# Also, the characters between the third and fourth '|' are excluded from the answer.
# There are 2 asterisks considered. Therefore, we return 2.
# Example 2:

# Input: s = "iamprogrammer"
# Output: 0
# Explanation: In this example, there are no asterisks in s. Therefore, we return 0.
# Example 3:

# Input: s = "yo|uar|e**|b|e***au|tifu|l"
# Output: 5
# Explanation: The considered characters are underlined: "yo|uar|e**|b|e***au|tifu|l". There are 5 asterisks considered. Therefore, we return 5.
 

# Constraints:

# 1 <= s.length <= 1000
# s consists of lowercase English letters, vertical bars '|', and asterisks '*'.
# s contains an even number of vertical bars '|'.


# sol 1
# class Solution:
#     def countAsterisks(self, s: str) -> int:
#         count = 0
#         c = 0
#         for i in s:
#             if i == '|':
#                 count += 1
#             elif i == '*' and count%2==0:
#                 c += 1
#         return c
        

# sol 2
# class Solution:
#     def countAsterisks(self, s: str) -> int:
#         ans,t = 0,0
#         for i in s:
#             if i == "|":
#                 t += 1
#             elif t % 2 ==0:
#                 ans += i=="*"
#         return ans

# sol 3
# class Solution:
# 	"""
# 	Time:   O(n)
# 	Memory: O(n)
# 	"""
# 	def countAsterisks(self, s: str) -> int:
# 		return sum(chunk.count('*') for chunk in s.split('|')[0::2])

# sol 4
# class Solution:
# 	"""
# 	Time:   O(n)
# 	Memory: O(1)
# 	"""
# 	def countAsterisks(self, s: str) -> int:
# 		is_closed = True
# 		count = 0
# 		for c in s:
# 			count += is_closed * c == '*'
# 			is_closed ^= c == '|'
# 		return count

# sol 5
# class Solution:
#     def countAsterisks(self, s: str) -> int:
#         openBar = False
#         aster = 0
#         for char in s:
#             if char == "|":
#                 openBar = not openBar
#             elif char == "*" and not openBar:
#                 aster += 1
#         return aster

