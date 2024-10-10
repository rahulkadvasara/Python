# 485. Max Consecutive Ones
# Solved
# Easy

# Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.



# # sol 1

# class Solution:
#     def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#         max_c=0
#         curr=0
#         for i in range(len(nums)):
#             if(nums[i]==1):
#                 curr+=1
#                 max_c=max(max_c,curr)
#             else:
#                 curr=0
#         return max_c   


# # sol 2

# class Solution:
#     def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#         cntr = 0
#         max = 0
#         for i in nums:
#             if i == 0:
#                 cntr = 0
#             else:
#                 cntr = cntr + 1
#             if cntr > max:
#                 max = cntr
#         return max
        

