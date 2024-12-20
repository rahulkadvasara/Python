# 1859. Sorting the Sentence
# Easy
# A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of lowercase and uppercase English letters.
# A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.
# For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
# Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.

# Example 1:
# Input: s = "is2 sentence4 This1 a3"
# Output: "This is a sentence"
# Explanation: Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.

# Example 2:
# Input: s = "Myself2 Me1 I4 and3"
# Output: "Me Myself and I"
# Explanation: Sort the words in s to their original positions "Me1 Myself2 and3 I4", then remove the numbers.
 
# Constraints:
# 2 <= s.length <= 200
# s consists of lowercase and uppercase English letters, spaces, and digits from 1 to 9.
# The number of words in s is between 1 and 9.
# The words in s are separated by a single space.
# s contains no leading or trailing spaces.



# sol 1

# class Solution:
#     def sortSentence(self, s: str) -> str:
#         arr = [(w[-1], w[:-1]) for w in s.split(" ")]
#         arr.sort()
#         return " ".join([w for _, w in arr])



# sol 2

# class Solution:
#     def sortSentence(self, s: str) -> str:
#         return " ".join([w for _, w in sorted([(w[-1], w[:-1]) for w in s.split(" ")])])
    

# sol 3

# class Solution:
#     def sortSentence(self, s: str) -> str:
#         words = s.split()
#         res = ''
#         for i in range(0, len(words)):
#             for j in range(i, len(words)):
#                 if int(words[i][-1]) > int(words[j][-1]):
#                     cont = words[j]
#                     words[j] = words[i]
#                     words[i] = cont
#         for i, word in enumerate(words):
#             if i == 0:
#                 res += word[:-1]
#             else:
#                 res += " " + word[:-1]
#         return res