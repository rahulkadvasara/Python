# 1608. Special Array With X Elements Greater Than or Equal X
# Easy
# You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.
# Notice that x does not have to be an element in nums.
# Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.

# Example 1:
# Input: nums = [3,5]
# Output: 2
# Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.

# Example 2:
# Input: nums = [0,0]
# Output: -1
# Explanation: No numbers fit the criteria for x.
# If x = 0, there should be 0 numbers >= x, but there are 2.
# If x = 1, there should be 1 number >= x, but there are 0.
# If x = 2, there should be 2 numbers >= x, but there are 0.
# x cannot be greater since there are only 2 numbers in nums.

# Example 3:
# Input: nums = [0,4,3,0,4]
# Output: 3
# Explanation: There are 3 values that are greater than or equal to 3.

# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000



# sol 1

# import bisect
# class Solution:
#     def specialArray(self, nums: List[int]) -> int:
#         nums=sorted(nums)
#         n=len(nums)
#         for i in range(n,0,-1):
#             k=bisect.bisect_left(nums,i)
#             if(n-k==i):
#                 return i
#         return -1



# sol 2

# class Solution:
#     def specialArray(self, nums: List[int]) -> int:
#         count = Counter(nums)
#         total_so_far = 0
#         for i in range(max(nums),-1,-1):
#             total_so_far += count[i]
#             if total_so_far==i:
#                 return i
#         return -1
    


# sol 3

# class Solution:
#     def specialArray(self, nums: List[int]) -> int:
#         nums.sort(reverse=True)
#         for x in range(1, len(nums) + 1):
#             if nums[x-1] >= x and (x == len(nums) or nums[x] < x):
#                 return x
#         return -1



# sol 4

# class Solution:
#     def specialArray(self, nums: List[int]) -> int:
#         nums.sort()
#         if nums[0] >= len(nums):
#             return len(nums)
#         for i, (a, b) in enumerate(itertools.pairwise(nums)):
#             count = len(nums) - i - 1
#             if a < count and b >= count:
#                 return count
#         return -1