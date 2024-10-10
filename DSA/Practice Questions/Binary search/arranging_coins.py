# 441. Arranging Coins
# Easy

# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

# Given the integer n, return the number of complete rows of the staircase you will build.

# Example 1:

# Input: n = 5
# Output: 2
# Explanation: Because the 3rd row is incomplete, we return 2.

# Example 2:

# Input: n = 8
# Output: 3
# Explanation: Because the 4th row is incomplete, we return 3.
 

# Constraints:

# 1 <= n <= 231 - 1


# sol 1

# class Solution:
#     def arrangeCoins(self, n: int) -> int:        
#         i=0
#         while n>=0:
#             i+=1
#             n=n-i
#         return i-1


# sol 2

# class Solution:
#     def arrangeCoins(self, n: int) -> int:
#         if n==1:return n
#         for i in range(1,n+1):
#             n=n-i
#             if n<0: return i-1


# sol 3

# class Solution:
#     def arrangeCoins(self, n: int) -> int:
#         left,right=1,n
#         while left<=right:
#             mid=(right+left)//2
#             num=(mid/2)*(mid+1)
#             if num<=n:
#                 left=mid+1
#             else:
#                 right=mid-1
#         return right


