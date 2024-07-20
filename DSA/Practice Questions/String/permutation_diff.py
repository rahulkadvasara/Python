# 3146. Permutation Difference between Two Strings

# You are given two strings s and t such that every character occurs at most once in s and t is a permutation of s.

# The permutation difference between s and t is defined as the sum of the absolute difference between the index of the occurrence of each character in s and the index of the occurrence of the same character in t.

# Return the permutation difference between s and t.

 

# Example 1:

# Input: s = "abc", t = "bac"

# Output: 2

# Explanation:

# For s = "abc" and t = "bac", the permutation difference of s and t is equal to the sum of:

# The absolute difference between the index of the occurrence of "a" in s and the index of the occurrence of "a" in t.
# The absolute difference between the index of the occurrence of "b" in s and the index of the occurrence of "b" in t.
# The absolute difference between the index of the occurrence of "c" in s and the index of the occurrence of "c" in t.
# That is, the permutation difference between s and t is equal to |0 - 1| + |2 - 2| + |1 - 0| = 2.

# Example 2:

# Input: s = "abcde", t = "edbac"

# Output: 12

# Explanation: The permutation difference between s and t is equal to |0 - 3| + |1 - 2| + |2 - 4| + |3 - 1| + |4 - 0| = 12.

 

# Constraints:

# 1 <= s.length <= 26
# Each character occurs at most once in s.
# t is a permutation of s.
# s consists only of lowercase English letters

# sol 1
# class Solution:
#     def findPermutationDifference(self, s: str, t: str) -> int:
#         ht: dict[str, int] = dict()
#         for i in range(len(s)):
#             if s[i] in ht:
#                 ht[s[i]] = abs(ht[s[i]] - i)
#             else:
#                 ht[s[i]] = i
#             if t[i] in ht:
#                 ht[t[i]] = abs(ht[t[i]] - i)
#             else:
#                 ht[t[i]] = i
#         return sum(ht.values())

# sol 2
# class Solution:
#     def findPermutationDifference(self, s: str, t: str) -> int:
#         ind_s={c:i for i,c in enumerate(s)}
#         ind_t={c:i for i,c in enumerate(t)}
#         d=0
#         for char in s:
#             d+=abs(ind_s[char]-ind_t[char])
#         return d

# sol 3
# class Solution:
#     def findPermutationDifference(self, s: str, t: str) -> int:
#         pos = {ch : i for i, ch in enumerate(t)}
#         return sum([abs(i - pos[s[i]]) for i in range(len(s))])

# sol 4
# class Solution:
#     def findPermutationDifference(self, s: str, t: str) -> int:
#         score = 0
#         for index,ch in enumerate(s):
#             score += abs(t.find(ch)-index)
#         return score


# sol 1
# class Solution:
#     def mostWordsFound(self, sentences: List[str]) -> int:
#         return max(s.count(" ") for s in sentences)+1

# sol 2
# class Solution:
#     def mostWordsFound(self, sentences: List[str]) -> int:
#         max = 0
#         for e in sentences:
#             s = e.split()
#             if len(s) > max:
#                 max = len(s)
#         return max
