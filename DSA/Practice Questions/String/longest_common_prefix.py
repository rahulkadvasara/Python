# 14. Longest Common Prefix
# Easy

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.



# sol 1

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         pre = strs[0]
#         pre_len = len(pre)
#         for s in strs[1:]:
#             while pre != s[0:pre_len]:
#                 pre_len -= 1
#                 if pre_len == 0:
#                     return ""
#                 pre = pre[0:pre_len]
#         return pre