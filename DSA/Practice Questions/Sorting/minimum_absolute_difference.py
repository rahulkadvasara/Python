# 1200. Minimum Absolute Difference
# Easy
# Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.
# Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
# a, b are from arr
# a < b
# b - a equals to the minimum absolute difference of any two elements in arr
 
# Example 1:
# Input: arr = [4,2,1,3]
# Output: [[1,2],[2,3],[3,4]]
# Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.

# Example 2:
# Input: arr = [1,3,6,10,15]
# Output: [[1,3]]

# Example 3:
# Input: arr = [3,8,-10,23,19,-4,-14,27]
# Output: [[-14,-10],[19,23],[23,27]]
 
# Constraints:
# 2 <= arr.length <= 105
# -106 <= arr[i] <= 106



# sol 1

# class Solution:
#     def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
#         indx = []
#         arr.sort()
#         mabs = arr[1] - arr[0]
#         for i in range(len(arr) - 1):
#             min_abs = abs(arr[i + 1] - arr[i])
#             if min_abs < mabs:
#                 mabs = min_abs
#                 indx.clear()
#                 indx.append([arr[i], arr[i + 1]])
#             elif min_abs == mabs:
#                 indx.append([arr[i], arr[i + 1]])
#         return indx
    
