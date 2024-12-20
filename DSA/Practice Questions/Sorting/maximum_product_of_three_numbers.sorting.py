# 628. Maximum Product of Three Numbers

# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

# Example 1:
# Input: nums = [1,2,3]
# Output: 6

# Example 2:
# Input: nums = [1,2,3,4]
# Output: 24

# Example 3:
# Input: nums = [-1,-2,-3]
# Output: -6
 
# Constraints:
# 3 <= nums.length <= 104
# -1000 <= nums[i] <= 1000



# sol 1

# class Solution:
#     def maximumProduct(self, nums: List[int]) -> int:
#         first_max = float('-inf')
#         second_max = first_max
#         third_max = first_max
#         first_min = float('inf')
#         second_min = first_min
#         for i in range(len(nums)):
#             if first_max <= nums[i]:
#                 third_max = second_max
#                 second_max = first_max
#                 first_max = nums[i]
#             elif second_max <= nums[i]:
#                 third_max = second_max
#                 second_max = nums[i]
#             elif third_max <= nums[i]:
#                 third_max = nums[i]
#             if(first_min >= nums[i]):
#                 second_min = first_min
#                 first_min = nums[i]
#             elif second_min >= nums[i]:
#                 second_min = nums[i]
#         return max(first_max * second_max * third_max, first_min * second_min * first_max)
    

# sol 2

# class Solution:
#     def maximumProduct(self, nums: List[int]) -> int:
#         nums.sort()
#         return max(nums[-1]*nums[-2]*nums[-3],nums[0]*nums[1]*nums[-1])