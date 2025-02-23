# 3350. Adjacent Increasing Subarrays Detection II
# Medium

# Given an array nums of n integers, your task is to find the maximum value of k for which there exist two adjacent 
# subarrays
#  of length k each, such that both subarrays are strictly increasing. Specifically, check if there are two subarrays of length k starting at indices a and b (a < b), where:
# Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
# The subarrays must be adjacent, meaning b = a + k.
# Return the maximum possible value of k.
# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:
# Input: nums = [2,5,7,8,9,2,3,4,3,1]
# Output: 3
# Explanation:
# The subarray starting at index 2 is [7, 8, 9], which is strictly increasing.
# The subarray starting at index 5 is [2, 3, 4], which is also strictly increasing.
# These two subarrays are adjacent, and 3 is the maximum possible value of k for which two such adjacent strictly increasing subarrays exist.

# Example 2:
# Input: nums = [1,2,3,4,4,4,4,5,6,7]
# Output: 2
# Explanation:
# The subarray starting at index 0 is [1, 2], which is strictly increasing.
# The subarray starting at index 2 is [3, 4], which is also strictly increasing.
# These two subarrays are adjacent, and 2 is the maximum possible value of k for which two such adjacent strictly increasing subarrays exist.

# Constraints:
# 2 <= nums.length <= 2 * 105
# -109 <= nums[i] <= 109



# sol 1

# class Solution:
#     def maxIncreasingSubarrays(self, nums: List[int]) -> int:
#         prev_increase, cur_increase = 0,1
#         res = 0
#         for i in range(1, len(nums)):
#             if nums[i] > nums[i - 1]: cur_increase += 1
#             else: prev_increase, cur_increase = cur_increase, 1
#             res = max(res, cur_increase // 2, min(prev_increase, cur_increase))
#         return res



# sol 2

# class Solution:
#     def maxIncreasingSubarrays(self, nums: List[int]) -> int:
#         n = len(nums)
#         left = [0] * n
#         right = [0] * n
#         for i in range(1, n):
#             left[i] = left[i - 1] + 1 if nums[i] > nums[i - 1] else 0
#         for i in range(n - 2, -1, -1):
#             right[i] = right[i + 1] + 1 if nums[i] < nums[i + 1] else 0
#         res = 0
#         for i in range(1, n):
#             res = max(res, min(left[i], right[i]))
#         return res



# sol 3

# class Solution:
#     def maxIncreasingSubarrays(self, nums: List[int]) -> int:
#         n = len(nums)
#         f = [0] * (n + 2)
#         g = [0] * (n + 2)
        
#         f[0] = 0
#         for i in range(1, n + 1):
#             if i > 1 and nums[i - 2] < nums[i - 1]:
#                 f[i] = f[i - 1] + 1
#             else:
#                 f[i] = 1
        
#         for i in range(n, 0, -1):
#             if i < n and nums[i - 1] < nums[i]:
#                 g[i] = g[i + 1] + 1
#             else:
#                 g[i] = 1
        
#         ans = 0
#         for i in range(1, n + 1):
#             ans = max(ans, min(f[i - 1], g[i]))
        
#         return ans



# sol 4

# class Solution:
#     def check(self, v, k):
#         for i in range(len(v) - k):
#             if v[i] >= k and v[i + k] >= k:
#                 return True
#         return False

#     def maxIncreasingSubarrays(self, nums):
#         n = len(nums)
#         if n == 2:
#             return 1

#         dp = [1] * n
#         for i in range(1, n):
#             if nums[i] <= nums[i - 1]:
#                 dp[i] = 1
#             else:
#                 dp[i] = dp[i - 1] + 1

#         ans = 1
#         low, high = 1, n // 2

#         while low <= high:
#             mid = low + (high - low) // 2
#             if self.check(dp, mid):
#                 ans = mid
#                 low = mid + 1
#             else:
#                 high = mid - 1
#         return ans



# sol 5

# class Solution:
#     def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        
#         inc = []

#         inc_count = 1
#         for i in range(1, len(nums)):
#             if nums[i] > nums[i - 1] :
#                 inc_count += 1
#             else:
#                 inc.append(inc_count)
#                 inc_count = 1
#         inc.append(inc_count)
#         max_ctn = inc[0]
#         max_ctg = 0

#         for i in range(1, len(inc)):
#             if inc[i] > max_ctn:
#                 max_ctn = inc[i]
#             if min(inc[i-1], inc[i]) > max_ctg:
#                 max_ctg = min(inc[i-1], inc[i])
        
#         return max(max_ctg, max_ctn // 2)