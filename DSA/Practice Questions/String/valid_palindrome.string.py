# 125. Valid Palindrome
# Easy

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 
# Constraints:
# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.



# sol 1

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         l = 0
#         r = len(s) - 1
#         while l < r:
#             if not s[l].isalnum():
#                 l += 1
#             elif not s[r].isalnum():
#                 r -= 1
#             elif s[l].lower() == s[r].lower():
#                 l += 1
#                 r -= 1
#             else:
#                 return False

#         return True


# sol 2

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = [c.lower() for c in s if c.isalnum()]
#         return all (s[i] == s[~i] for i in range(len(s)//2))
    

# sol 3

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         i, j = 0, len(s) - 1
#         while i < j:
#             while i < j and not s[i].isalnum(): i += 1
#             while i < j and not s[j].isalnum(): j -= 1

#             if s[i].lower() != s[j].lower(): return False
#             i += 1
#             j -= 1

#         return True
    

# sol 4

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         string=[]
#         for i in s:
#             if i.isalnum():
#                 string.append(i.lower())
#             else:
#                 continue
#         index_comp=(len(string)+1)//2
#         for i in range(index_comp):
#             if string[i]==string[len(string)-1-i]:
#                 continue
#             else:
#                 return False
#         return True
    

# sol 5

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = s.lower().replace(' ','')
#         s = [c for c in s if c.isalnum()]
#         return s == s[::-1]