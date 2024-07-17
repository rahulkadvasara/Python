# 2006. Count Number of Pairs With Absolute Difference K
# Easy
# Topics
# Companies
# Hint
# Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.

# The value of |x| is defined as:

# x if x >= 0.
# -x if x < 0.
 

# Example 1:

# Input: nums = [1,2,2,1], k = 1
# Output: 4
# Explanation: The pairs with an absolute difference of 1 are:
# - [1,2,2,1]
# - [1,2,2,1]
# - [1,2,2,1]
# - [1,2,2,1]
# Example 2:

# Input: nums = [1,3], k = 3
# Output: 0
# Explanation: There are no pairs with an absolute difference of 3.
# Example 3:

# Input: nums = [3,2,1,5,4], k = 2
# Output: 3
# Explanation: The pairs with an absolute difference of 2 are:
# - [3,2,1,5,4]
# - [3,2,1,5,4]
# - [3,2,1,5,4]
 

# Constraints:

# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100
# 1 <= k <= 99

# sol 1
# class Solution:
#     def countKDifference(self, nums: List[int], k: int) -> int:
#         op=0
#         for i in range(len(nums)):
#             for j in range(1,len(nums)):
#                 if abs(nums[i]-nums[j])==k:
#                     op+=1
#                     break
#         return op

# sol 2
# class Solution:
#     def countKDifference(self, nums: List[int], k: int) -> int:
#         c = 0
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if abs(nums[i] - nums[j]) == k:
#                     c += 1
#         return c

# sol 3
# class Solution:
#     def countKDifference(self, nums: List[int], k: int) -> int:
#         seen = defaultdict(int)
#         counter = 0
#         for num in nums:
#             tmp, tmp2 = num - k, num + k
#             if tmp in seen:
#                 counter += seen[tmp]
#             if tmp2 in seen:
#                 counter += seen[tmp2]
            
#             seen[num] += 1
        
#         return counter

# sol 4
# class Solution:
#     def countKDifference(self, nums: List[int], k: int) -> int:
#         seen = defaultdict(int)
#         counter = 0
#         for num in nums:
#             counter += seen[num-k] + seen[num+k]
#             seen[num] += 1
#         return counter

# sol 5
# def countKDifference(self, nums: List[int], k: int) -> int:
#         seen, cnt = dict(), 0
#         for x in nums:
#             cnt += seen.get(x-k,0) + seen.get(x+k,0)
#             seen[x] = seen.get(x,0) + 1
#         return cnt

# sol 6 
# class Solution:
#     def countKDifference(self, nums: List[int], k: int) -> int:
#         count = 0
#         hm = {}

#         for num in nums:
#             if num not in hm:
#                 hm[num] = 1
#             else:
#                 hm[num] += 1

#         for num in nums:
#             if num + k in hm:
#                 count += hm[num + k]

#         return count

# sol 7
# from collections import defaultdict
# class Solution:
#     def countKDifference(self, nums: List[int], k: int) -> int:
#         count = 0
#         freq_diff = defaultdict(int)
#         for num in nums:
#             if abs(num - k) in freq_diff:
#                 count += freq_diff[num - k]
#             if abs(num + k) in freq_diff:
#                 count += freq_diff[num + k]
#             freq_diff[num] += 1
#         return count

# sol 8


