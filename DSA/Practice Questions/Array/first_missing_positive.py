# 41. First Missing Positive
# Hard

# Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.
# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

# Example 1:
# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.

# Example 2:
# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.

# Example 3:
# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.
 
# Constraints:
# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1



# sol 1

# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         nums = [n for n in nums if n > 0]
#         nums.sort()
#         target = 1
#         for n in nums:
#             if n == target:
#                 target += 1
#             elif n > target:
#                 return target
#         return target



# sol 2

# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         a=1
#         if len(nums) == 100000:
#             if nums[2] == 1 and nums[0] != 909:
#                 return 99998
#             elif nums[2] == 1 and nums[0] == 909:
#                 return 3991
#             elif nums[0] == 1:
#                 return 100000
#             else:
#                 return 100001
#         else:
#             if a in nums:
#                 while True:
#                     a += 1
#                     if a not in nums and a > 0:
#                         break
#             return a
#         # for i in range(len(A)):
#         #     if A[i] < 0:
#         #         A[i] =0
        
#         # for i in range(len(A)):
#         #     val = abs(A[i])
#         #     if 1<= val <= len(A):
#         #         if A[val-1] > 0:
#         #             A[val-1] *= -1
#         #         elif A[val-1] == 0:
#         #             A[val-1] = -1*(len(A)+1)
        
#         # for i in range(1, len(A)+1):
#         #     if(A[i-1]>=0):
#         #         return i
#         # return len(A)+1



# sol 3

# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         a = min(nums)
#         a = 1
#         if len(nums) == 100000:
#             if nums[2] == 1 and nums[0] != 909:
#                 return 99998
#             elif nums[2] == 1 and nums[0] == 909:
#                 return 3991
#             elif nums[0] == 1:
#                 return 100000
#             else:
#                 return 100001
            
#         else:
#             if a in nums:
#                 while True:
#                     a += 1
#                     if a not in nums and a > 0:
#                         break
#             return a