# 6. Zigzag Conversion
# Medium

# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
 

# Example 1:
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"

# Example 2:
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

# Example 3:
# Input: s = "A", numRows = 1
# Output: "A"
 
# Constraints:
# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000



# sol 1

# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         if numRows == 1 or numRows >= len(s):
#             return s
#         idx, d = 0, 1
#         rows = [[] for _ in range(numRows)]
#         for char in s:
#             rows[idx].append(char)
#             if idx == 0:
#                 d = 1
#             elif idx == numRows - 1:
#                 d = -1
#             idx += d
#         for i in range(numRows):
#             rows[i] = ''.join(rows[i])
#         return ''.join(rows)   


# sol 2

# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         if numRows == 1:
#             return s

#         rows = [""] * numRows
        
#         add = 0
#         inc = 1
#         for i in s:
#             rows[add] += i
#             if add == 0:
#                 inc = 1
#             elif add == numRows - 1:
#                 inc = -1

#             add += inc
            
#         return "".join(rows)