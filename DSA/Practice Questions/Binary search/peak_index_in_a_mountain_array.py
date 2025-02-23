# 852. Peak Index in a Mountain Array
# Medium

# You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.
# Return the index of the peak element.
# Your task is to solve it in O(log(n)) time complexity.

# Example 1:
# Input: arr = [0,1,0]
# Output: 1

# Example 2:
# Input: arr = [0,2,1,0]
# Output: 1

# Example 3:
# Input: arr = [0,10,5,2]
# Output: 1

# Constraints:
# 3 <= arr.length <= 105
# 0 <= arr[i] <= 106
# arr is guaranteed to be a mountain array.



# sol 1

# class Solution:
#     def peakIndexInMountainArray(self, arr: List[int]) -> int:
#         start=0
#         end=len(arr)-1
#         while(start<end):
#             mid=(start+end)//2
#             if(arr[mid]>arr[mid+1]):
#                 end=mid
#             else:
#                 start=mid+1
#         return end