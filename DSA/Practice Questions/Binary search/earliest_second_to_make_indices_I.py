# 3048. Earliest Second to Mark Indices I
# Medium

# You are given two 1-indexed integer arrays, nums and, changeIndices, having lengths n and m, respectively.
# Initially, all indices in nums are unmarked. Your task is to mark all indices in nums.
# In each second, s, in order from 1 to m (inclusive), you can perform one of the following operations:
# Choose an index i in the range [1, n] and decrement nums[i] by 1.
# If nums[changeIndices[s]] is equal to 0, mark the index changeIndices[s].
# Do nothing.
# Return an integer denoting the earliest second in the range [1, m] when all indices in nums can be marked by choosing operations optimally, or -1 if it is impossible.

# Example 1:
# Input: nums = [2,2,0], changeIndices = [2,2,2,2,3,2,2,1]
# Output: 8
# Explanation: In this example, we have 8 seconds. The following operations can be performed to mark all indices:
# Second 1: Choose index 1 and decrement nums[1] by one. nums becomes [1,2,0].
# Second 2: Choose index 1 and decrement nums[1] by one. nums becomes [0,2,0].
# Second 3: Choose index 2 and decrement nums[2] by one. nums becomes [0,1,0].
# Second 4: Choose index 2 and decrement nums[2] by one. nums becomes [0,0,0].
# Second 5: Mark the index changeIndices[5], which is marking index 3, since nums[3] is equal to 0.
# Second 6: Mark the index changeIndices[6], which is marking index 2, since nums[2] is equal to 0.
# Second 7: Do nothing.
# Second 8: Mark the index changeIndices[8], which is marking index 1, since nums[1] is equal to 0.
# Now all indices have been marked.
# It can be shown that it is not possible to mark all indices earlier than the 8th second.
# Hence, the answer is 8.

# Example 2:
# Input: nums = [1,3], changeIndices = [1,1,1,2,1,1,1]
# Output: 6
# Explanation: In this example, we have 7 seconds. The following operations can be performed to mark all indices:
# Second 1: Choose index 2 and decrement nums[2] by one. nums becomes [1,2].
# Second 2: Choose index 2 and decrement nums[2] by one. nums becomes [1,1].
# Second 3: Choose index 2 and decrement nums[2] by one. nums becomes [1,0].
# Second 4: Mark the index changeIndices[4], which is marking index 2, since nums[2] is equal to 0.
# Second 5: Choose index 1 and decrement nums[1] by one. nums becomes [0,0].
# Second 6: Mark the index changeIndices[6], which is marking index 1, since nums[1] is equal to 0.
# Now all indices have been marked.
# It can be shown that it is not possible to mark all indices earlier than the 6th second.
# Hence, the answer is 6.

# Example 3:
# Input: nums = [0,1], changeIndices = [2,2,2]
# Output: -1
# Explanation: In this example, it is impossible to mark all indices because index 1 isn't in changeIndices.
# Hence, the answer is -1.

# Constraints:
# 1 <= n == nums.length <= 2000
# 0 <= nums[i] <= 109
# 1 <= m == changeIndices.length <= 2000
# 1 <= changeIndices[i] <= n



# sol 1

# class Solution:
#     def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
#         left, right = 0, len(changeIndices)+1
#         while left < right:
#             mid = left + (right-left)//2
#             if self.isOK(mid, nums, changeIndices):
#                 right = mid
#             else:
#                 left = mid+1
#         if left == len(changeIndices)+1: return -1
#         return left
            
            
#     def isOK(self, steps, nums, changeIndices):
#         n = len(nums)
#         visited = set()
#         ops = 0
#         for i in range(steps-1, -1, -1):
#             j = changeIndices[i]
#             if j not in visited:
#                 ops += nums[j-1]
#                 visited.add(j)
#             elif ops:
#                 ops -= 1
#         if len(visited) < n: return False
#         return ops == 0



# sol 2

# class Solution:
#     def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
#         n, m = len(nums), len(changeIndices)
#         if len(set(changeIndices)) < n or sum(nums) + n > m:
#             return -1
#         indices = [list() for _ in range(n+1)]
#         for i, v in enumerate(changeIndices):
#             indices[v].append(i)

#         for end in range(sum(nums) + n - 1, m):
#             last_indices = []
#             for v in range(1, n+1):
#                 idx = bisect.bisect_right(indices[v], end) - 1
#                 if idx < 0:
#                     break
#                 last_indices.append(indices[v][idx])
#             if len(last_indices) < n:
#                 continue
#             last_indices.sort()
#             s = 0
#             for idx in last_indices:
#                 if idx < s + nums[changeIndices[idx]-1]:
#                     break
#                 s += nums[changeIndices[idx]-1] + 1
#             else:
#                 return end + 1
#         return -1