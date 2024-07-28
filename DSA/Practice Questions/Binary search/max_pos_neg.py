# 2529. Maximum Count of Positive Integer and Negative Integer

# Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.

# In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.
# Note that 0 is neither positive nor negative.

 

# Example 1:

# Input: nums = [-2,-1,-1,1,2,3]
# Output: 3
# Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.
# Example 2:

# Input: nums = [-3,-2,-1,0,0,1,2]
# Output: 3
# Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.
# Example 3:

# Input: nums = [5,20,66,1314]
# Output: 4
# Explanation: There are 4 positive integers and 0 negative integers. The maximum count among them is 4.
 

# Constraints:

# 1 <= nums.length <= 2000
# -2000 <= nums[i] <= 2000
# nums is sorted in a non-decreasing order.
 

# Follow up: Can you solve the problem in O(log(n)) time complexity?

# sol 1
# O(n)
# class Solution:
#     def maximumCount(self, nums: List[int]) -> int:
#         mxP=0
#         mxN=0
#         for i in range(len(nums)):
#             if(nums[i]<0):
#                 mxN+=1
#             elif(nums[i]>0):
#                 mxP+=1
#         if(mxP>mxN):
#             return mxP
#         else:
#             return mxN

# sol 2
# class Solution:
#     def maximumCount(self, nums: List[int]) -> int:
#         return max(bisect_right(nums, -1), len(nums) - bisect_left(nums, 1))

# sol 3
# class Solution:
#     def maximumCount(self, nums: List[int]) -> int:
#         mxP=0
#         mxN=0
#         for i in range(len(nums)):
#             if(nums[i]<0):
#                 mxN+=1
#             elif(nums[i]>0):
#                 mxP+=1
#         return max(mxP,mxN)

# sol 3
# class Solution:
#     def maximumCount(self, nums: List[int]) -> int:
#         num_negative = len(list(filter(lambda x: x < 0, nums)))
#         num_positive = len(list(filter(lambda x: x > 0, nums)))
#         return max([num_negative, num_positive])

# sol 4
# class Solution:
#     def maximumCount(self, nums: List[int]) -> int:
#         return max(bisect.bisect_left(nums,0),len(nums)-bisect.bisect_right(nums,0))

