# 58. Length of Last Word

# Easy

# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal 
# substring
#  consisting of non-space characters only.

 

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
 

# Constraints:

# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.



# # sol 1

# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         words = s.strip().split()
#         if not words:
#             return 0
#         return len(words[-1])
    

# # sol 2

# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         i = len(s) - 1
#         while s[i] == " ":
#             i -= 1
#         x = i
#         while x >= 0 and s[x] != " ":
#             x -= 1
#         return i - x
    

# # sol 3

# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         words = s.strip().split()
#         return len(words[len(words) - 1])