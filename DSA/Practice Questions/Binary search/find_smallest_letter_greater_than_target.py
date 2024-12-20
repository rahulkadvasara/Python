# 744. Find Smallest Letter Greater Than Target
# Easy
# You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.
# Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

# Example 1:
# Input: letters = ["c","f","j"], target = "a"
# Output: "c"
# Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.

# Example 2:
# Input: letters = ["c","f","j"], target = "c"
# Output: "f"
# Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.

# Example 3:
# Input: letters = ["x","x","y","y"], target = "z"
# Output: "x"
# Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].
 
# Constraints:
# 2 <= letters.length <= 104
# letters[i] is a lowercase English letter.
# letters is sorted in non-decreasing order.
# letters contains at least two different characters.
# target is a lowercase English letter.



# sol 1

# class Solution:
#     def nextGreatestLetter(self, letters: List[str], target: str) -> str:
#         for i in letters:
#             if i>target:
#                 return i
#         return letters[0]
    

# sol 2

# class Solution(object):
#     def nextGreatestLetter(self, letters, target):
#         n=len(letters)
#         res='{'
#         for i in range(n):
#             if(res>letters[i] and letters[i]>target):
#                 res=letters[i]
#         if(res=='{'):
#             return letters[0]
#         return res
    


# sol 3

# class Solution(object):
#     def nextGreatestLetter(self, letters, target):
#         if target >= letters[-1] or target < letters[0]:
#             return letters[0]
#         low = 0
#         high = len(letters)-1
#         while low <= high:
#             mid = (high+low)//2
#             if  target >= letters[mid]:
#                 low = mid+1
#             if target < letters[mid]:
#                 high = mid-1
#         return letters[low]
