# 2574. Left and Right Sum Differences
# Attempted
# Easy
# Topics
# Companies
# Hint
# Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:

# answer.length == nums.length.
# answer[i] = |leftSum[i] - rightSum[i]|.
# Where:

# leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
# rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
# Return the array answer.

 

# Example 1:

# Input: nums = [10,4,8,3]
# Output: [15,1,11,22]
# Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
# The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].
# Example 2:

# Input: nums = [1]
# Output: [0]
# Explanation: The array leftSum is [0] and the array rightSum is [0].
# The array answer is [|0 - 0|] = [0].
 

# Constraints:

# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 105


# sol 1
# class Solution:
#     def leftRightDifference(self, nums: List[int]) -> List[int]:
#         leftSum=[0]
#         rightSum=[0]*len(nums)
#         op=[0]*len(nums)
#         sumL=0
#         sumR=0
#         for i in range(len(nums)):
#             if i==0:
#                 leftSum[0]=0
#                 sumL+=nums[0]
#             else:
#                 leftSum.append(sumL)
#                 sumL+=nums[i]
#         for i in range(len(nums)-1,-1,-1):
#             if i==len(nums)-1:
#                 rightSum[len(nums)-1]=0
#                 sumR+=nums[len(nums)-1]
#             else:
#                 rightSum[i]=sumR
#                 sumR+=nums[i]
#         for i in range(len(nums)):
#             op[i]=abs(rightSum[i]-leftSum[i])
#         #     if op[i]<0:
#         #         op[i]*=-1
#         return op


# sol 2
# # from typing import List
# class Solution:
#     def leftRightDifference(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         right = sum(nums)  # Calculate the sum of all elements
#         left = 0
#         res = []
#         for i in range(n):
#             right -= nums[i]  # Subtract the current element from the right sum
#             res.append(abs(left - right))  # Calculate the absolute difference and add it to the result list
#             left += nums[i]  # Add the current element to the left sum
#         return res

# sol 3
# class Solution:
#     def leftRigthDifference(self, nums: List[int]) -> List[int]:
#         prefix = 0 
#         suffix = sum(nums)
#         ans = []
#         for x in nums: 
#             prefix += x
#             ans.append(abs(prefix - suffix))
#             suffix -= x
#         return ans 

# sol 4
# class Solution:
#     def leftRightDifference(self, nums: List[int]) -> List[int]:
#         total = sum(nums)
#         res = []
#         prefix = 0
#         for i in range(len(nums)):
#             res.append(abs(prefix - (total - nums[i] - prefix)))
#             prefix += nums[i]
#         return res


# sol 5
# class Solution:
#     def leftRightDifference(self, nums: List[int]) -> List[int]:
#         import numpy as np
#         l1=[]
#         for i in range(len(nums)):
#             #print(i)
#             if i==0:
#                 l1.append(np.abs(0-sum(nums[i+1:])))
#             elif i==len(nums)-1:
#                 l1.append(np.abs(0-sum(nums[:i])))
#             else:
#                 print(sum(nums[0:i]))
#                 print(sum(nums[i+1:]))
#                 l1.append(np.abs(sum(nums[0:i])-sum(nums[i+1:])))
#         return l1



