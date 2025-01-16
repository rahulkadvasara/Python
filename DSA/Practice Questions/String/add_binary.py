# # 67. Add Binary
# # Easy

# # Given two binary strings a and b, return their sum as a binary string.

# # Example 1:
# # Input: a = "11", b = "1"
# # Output: "100"

# # Example 2:
# # Input: a = "1010", b = "1011"
# # Output: "10101"

# # Constraints:
# # 1 <= a.length, b.length <= 104
# # a and b consist only of '0' or '1' characters.
# # Each string does not contain leading zeros except for the zero itself.



# # sol 1

# # class Solution:
# #     def addBinary(self, a: str, b: str) -> str:
# #         return bin(int(a,2)+int(b,2))[2:]


# sol 2

# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         res = ''
#         carry = 0
#         i = len(a)-1
#         j = len(b)-1
#         while i >= 0 or j >= 0:
#             sum = carry
#             if i >= 0:
#                 sum += int(a[i])
#                 i -= 1
#             if j >= 0:
#                 sum += int(b[j])
#                 j -= 1
#             res = str(sum % 2) + res
#             carry = sum // 2
#         if carry:
#             res = '1' + res
#         return res



# sol 3

# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         n = max(len(a), len(b))
#         a, b = a.zfill(n), b.zfill(n)

#         carry = 0
#         result = []

#         for i in range(n-1, -1, -1):
#             if a[i] == "1":
#                 carry += 1
#             if b[i] == "1":
#                 carry += 1
            
#             if carry % 2 == 1:
#                 result.append("1")
#             else:
#                 result.append("0")
            
#             carry //= 2
        
#         if carry == 1:
#             result.append("1")

#         result.reverse()
#         return "".join(result)
