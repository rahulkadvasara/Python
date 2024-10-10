# 283. Move Zeroes
# Solved
# Easy

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1



# # sol 1

# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         i = 0

#         for j in range(len(nums)):
#             if nums[j] != 0:
#                 nums[j], nums[i] = nums[i], nums[j]
#                 i += 1
        
#         return nums