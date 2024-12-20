# 520. Detect Capital
# Easy
# We define the usage of capitals in a word to be right when one of the following cases holds:
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.

# Example 1:
# Input: word = "USA"
# Output: true

# Example 2:
# Input: word = "FlaG"
# Output: false
 
# Constraints:
# 1 <= word.length <= 100
# word consists of lowercase and uppercase English letters.



# sol 1

# class Solution:
#     def detectCapitalUse(self, word: str) -> bool:
#         return (word.upper() == word) or (word.lower() == word) or (word.capitalize() == word)
    

# sol 2

# class Solution:
#     def detectCapitalUse(self, word: str) -> bool:
#         flg=True
#         for i in word:
#             if i.islower() and flg==True:
#                 flg=False
#             if i.isupper() and flg==False:
#                 return False
#         flg=True
#         for i in range(len(word)-1,0,-1):
#             if word[i].islower() and flg==True:
#                 flg=False
#             if word[i].isupper() and flg==False:
#                 return False
#         return True