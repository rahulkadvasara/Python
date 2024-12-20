# 747. Largest Number At Least Twice of Others
# Easy
# You are given an integer array nums where the largest integer is unique.
# Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.

# Example 1:
# Input: nums = [3,6,1,0]
# Output: 1
# Explanation: 6 is the largest integer.
# For every other number in the array x, 6 is at least twice as big as x.
# The index of value 6 is 1, so we return 1.

# Example 2:
# Input: nums = [1,2,3,4]
# Output: -1
# Explanation: 4 is less than twice the value of 3, so we return -1.
 
# Constraints:
# 2 <= nums.length <= 50
# 0 <= nums[i] <= 100
# The largest element in nums is unique.



# sol 1

# class Solution(object):
#     def dominantIndex(self, nums):
#         n=len(nums)
#         fmax=-1
#         smax=-1
#         fmaxindex=-1
#         for i in range(n):
#             if(nums[i]>fmax):
#                 smax=fmax
#                 fmax=nums[i]
#                 fmaxindex=i
#             elif(nums[i]>smax):
#                 smax=nums[i]
#         if(fmax>=2*smax):
#             return fmaxindex
#         return -1
    

# sol 2

# class Solution:
#     def dominantIndex(self, nums: List[int]) -> int:
#         maxx,index=nums[0],0
#         for i,v in enumerate(nums):
#             maxx=max(maxx,v)
#             if maxx==v:
#                 index=i
#         for i in range(len(nums)):
#             if nums[i]!=maxx and maxx<2*nums[i]:
#                 return -1
#         return index
    

