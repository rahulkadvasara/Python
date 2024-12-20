# 345. Reverse Vowels of a String
# Easy
# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Example 1:
# Input: s = "IceCreAm"
# Output: "AceCreIm"

# Explanation:
# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"

# Constraints:
# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.




# sol 1

# class Solution:
#     def reverseVowels(self, s: str) -> str:
#         left = 0
#         right = len(s) - 1
#         s = list(s)
#         vowels = set('aeiouAEIOU')
#         while left < right:
#             while s[left] not in vowels and left < right:
#                 left += 1
#             while s[right] not in vowels and left < right:
#                 right -= 1
#             s[left], s[right] = s[right], s[left]
#             left += 1
#             right -= 1
#         return ''.join(s)
    


# sol 2

# class Solution:
#     def reverseVowels(self, s: str) -> str:
#         l=['a','e','i','o','u','A','E','I','O','U']
#         m=[]
#         for i in s:
#             if i in l:
#                 m.append(i)
#         n=len(m)
#         s=list(s)
#         for i in range(len(s)):
#             if s[i] in l:
#                 n-=1
#                 s[i]=m[n]
#         return ''.join(s)
                


