# 771. Jewels and Stones
# Easy
# Topics
# Companies
# Hint
# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

# Letters are case sensitive, so "a" is considered a different type of stone from "A".

 

# Example 1:

# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3
# Example 2:

# Input: jewels = "z", stones = "ZZ"
# Output: 0
 

# Constraints:

# 1 <= jewels.length, stones.length <= 50
# jewels and stones consist of only English letters.
# All the characters of jewels are unique

# sol 1
# class Solution:
#     def numJewelsInStones(self, jewels: str, stones: str) -> int:
#         c = 0
#         for i in range(len(jewels)):
#             for j in range(len(stones)):
#                 if(jewels[i]==stones[j]):
#                     c+=1
#         return c

# sol 2
# class Solution:
#     def numJewelsInStones(self, jw: str, st: str) -> int:
#         count = 0
#         for i in range(len(jw)):
#             for j in range(len(st)):
#                 if jw[i] is st[j]:
#                     count += 1
#         return count

# sol 3
# class Solution:
#     def numJewelsInStones(self, jewels: str, stones: str) -> int:
#         stonesDict = Counter(stones)
#         x = set(list(jewels))
#         count = 0
#         for i in range(len(stones)):
#             if stones[i] in x:
#                 count += 1
#         return count

        