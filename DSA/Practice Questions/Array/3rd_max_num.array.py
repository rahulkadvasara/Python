# 414. Third Maximum Number

# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

 

# Example 1:

# Input: nums = [3,2,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2.
# The third distinct maximum is 1.
# Example 2:

# Input: nums = [1,2]
# Output: 2
# Explanation:
# The first distinct maximum is 2.
# The second distinct maximum is 1.
# The third distinct maximum does not exist, so the maximum (2) is returned instead.
# Example 3:

# Input: nums = [2,2,3,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2 (both 2's are counted together since they have the same value).
# The third distinct maximum is 1.
 

# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1
 


# # sol 1

# class Solution:
#     def thirdMax(self, nums: List[int]) -> int:
#         a = list(set(nums))
#         b = sorted(a)
#         if len(b) < 3:
#             return b[-1]
#         else:
#             return b[-3]
        
# # sol 2

# class Solution:
#     def thirdMax(self, nums: List[int]) -> int:
#         a = set(nums)
#         if len(a)<3:
#             return max(a)
#         else:
#             a.remove(max(a))
#             a.remove(max(a))
#             return max(a)
        
# # sol 3

# class Solution:
#     def thirdMax(self, nums: List[int]) -> int:
#         nums=list(set(nums))
#         nums=sorted(nums)
    
#         if len(nums)>=3:
#             return nums[-3]
#         else:
#             return nums[-1]

# # sol 4

# class Solution:
#     def thirdMax(self, nums: List[int]) -> int:
#         uninum=list(set(nums))
#         uninum.sort(reverse=True)
#         if(len(uninum)>2):
#             ans=uninum[2]
#         else:
#             ans=uninum[0]
#         return ans
    
