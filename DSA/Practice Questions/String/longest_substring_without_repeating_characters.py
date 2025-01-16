# 3. Longest Substring Without Repeating Characters
# Medium

# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
# Constraints:
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.



# sol 1

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if not s:
#             return 0
#         start = 0
#         max_len = 0
#         seen = {}
#         for i in range(len(s)):
#             if s[i] in seen:
#                 start = max(start, seen[s[i]] + 1)
#             seen[s[i]] = i
#             max_len = max(max_len, i - start + 1)
#         return max_len