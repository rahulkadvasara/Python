# 16. 3Sum Closest
# Medium

# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.

# Example 1:
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# Example 2:
# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

# Constraints:
# 3 <= nums.length <= 500
# -1000 <= nums[i] <= 1000
# -104 <= target <= 104



# sol 1

# class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
#         nums.sort()
#         n = len(nums)
#         closest = float('inf')
#         for i in range(n):
#             l, r = i + 1, n - 1
#             while l < r:
#                 total = nums[i] + nums[l] + nums[r]
#                 if abs(total - target) < abs(closest - target):
#                     closest = total
#                 if total < target:
#                     l += 1
#                 else:
#                     r -= 1
#         return closest



# sol 2

# class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
#         nums.sort()
#         if sum(nums[:3]) >= target:
#             return sum(nums[:3])

#         if sum(nums[-3:]) <= target:
#             return sum(nums[-3:])

#         best = nums[0] + nums[1] + nums[2]
#         for i in range(len(nums)-2):
#             right = len(nums) - 1
#             left = i + 1
#             while left < right:
#                 sum1 = nums[i] + nums[left] + nums[right]
#                 if abs(target - sum1) < abs(target - best):
#                     best = sum1
#                 if sum1 < target:
#                     left += 1
#                 elif sum1 > target:
#                     right -= 1
#                 else:
#                     return best
#         return best