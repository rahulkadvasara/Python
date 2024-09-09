
# 1704. Determine if String Halves Are Alike
# Easy
# Topics
# Companies
# Hint
# You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

# Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

# Return true if a and b are alike. Otherwise, return false.

 

# Example 1:

# Input: s = "book"
# Output: true
# Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
# Example 2:

# Input: s = "textbook"
# Output: false
# Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
# Notice that the vowel o is counted twice.
 

# Constraints:

# 2 <= s.length <= 1000
# s.length is even.
# s consists of uppercase and lowercase letters.

# sol 1
# class Solution:
#     def halvesAreAlike(self, s: str) -> bool:
#         count1=0
#         count2=0
#         half=len(s)//2
#         for i in range(half):
#             if(s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u' or s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U'):
#                 count1+=1
#         for i in range(half,len(s)):
#             if(s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u' or s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U'):
#                 count2+=1
#         return count1==count2
        

# sol 2
# class Solution:
#     def halvesAreAlike(self, s: str) -> bool:
#         vowels = set('aeiouAEIOU')
#         size = len(s)
#         count = 0
        
#         for index in range(0, size//2):
#             if s[index] in vowels:
#                 count += 1

#             if s[index + size//2] in vowels:
#                 count -= 1
        
#         return count == 0

# sol 3
# class Solution:
#     def halvesAreAlike(self, s: str) -> bool:
#         cnt, cnt2, ln = 0, 0, len(s)
#         vowels = set('aeiouAEIOU')
#         for i in range(ln//2):
#             if s[i] in vowels: cnt += 1
#             if s[i+ln//2] in vowels: cnt2 += 1
#         return cnt == cnt2

# sol 4
# class Solution:
#     def cv(self,st):
#         c = 0
#         for i in st:
#             if i in 'aeiouAEIOU':
#                 c += 1
#         return c
#     def halvesAreAlike(self, s: str) -> bool:
#         return self.cv(s[:len(s)//2]) == self.cv(s[len(s)//2:])

