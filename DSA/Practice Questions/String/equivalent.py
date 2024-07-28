# 1662. Check If Two String Arrays are Equivalent

# Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

# A string is represented by an array if the array elements concatenated in order forms the string.

 

# Example 1:

# Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
# Output: true
# Explanation:
# word1 represents string "ab" + "c" -> "abc"
# word2 represents string "a" + "bc" -> "abc"
# The strings are the same, so return true.
# Example 2:

# Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
# Output: false
# Example 3:

# Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
# Output: true
 

# Constraints:

# 1 <= word1.length, word2.length <= 103
# 1 <= word1[i].length, word2[i].length <= 103
# 1 <= sum(word1[i].length), sum(word2[i].length) <= 103
# word1[i] and word2[i] consist of lowercase letters.

# sol 1
# class Solution:
#     def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
#         return all(starmap(eq, zip_longest(chain.from_iterable(word1), chain.from_iterable(word2))))

# sol 2 
# class Solution:
#     def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
#         w1, w2 = '', ''
#         for i in word1:
#             w1 += i
#         for j in word2:
#             w2 += j
#         return w1==w2

# sol 3
# class Solution:
#     def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
#         joined_word1 = "".join(word1)
#         joined_word2 = "".join(word2)
#         if (joined_word1==joined_word2):
#             return True
#         else:
#             return False    

