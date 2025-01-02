# 18. 4Sum
# Medium

# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

# Example 1:
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

# Example 2:
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
 
# Constraints:
# 1 <= nums.length <= 200
# -109 <= nums[i] <= 109
# -109 <= target <= 109



# sol 1

# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         nums.sort()
#         res = []
#         for i in range(len(nums)):
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue
#             for j in range(i+1, len(nums)):
#                 if j > i+1 and nums[j] == nums[j-1]:
#                     continue
#                 left, right = j+1, len(nums)-1
#                 while left < right:
#                     total = nums[i] + nums[j] + nums[left] + nums[right]
#                     if total == target:
#                         res.append([nums[i], nums[j], nums[left], nums[right]])
#                         left += 1
#                         right -= 1
#                         while left < right and nums[left] == nums[left-1]:
#                             left += 1
#                         while left < right and nums[right] == nums[right+1]:
#                             right -= 1
#                     elif total < target:
#                         left += 1
#                     else:
#                         right -= 1
#         return res



# sol 2

# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         # Sort array first to handle duplicates and enable two-pointer technique
#         nums.sort()
#         n = len(nums)
#         result = []
        
#         # Handle edge cases
#         if n < 4:
#             return result
            
#         for i in range(n - 3):
#             # Skip duplicates for first number
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue
                
#             # Early termination checks
#             # If smallest possible sum > target or largest possible sum < target
#             if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
#                 break
#             if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
#                 continue
                
#             for j in range(i + 1, n - 2):
#                 # Skip duplicates for second number
#                 if j > i + 1 and nums[j] == nums[j - 1]:
#                     continue
                    
#                 # Early termination checks for the second number
#                 if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
#                     break
#                 if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
#                     continue
                    
#                 # Use two pointers for the remaining elements
#                 left = j + 1
#                 right = n - 1
                
#                 while left < right:
#                     curr_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
#                     if curr_sum == target:
#                         result.append([nums[i], nums[j], nums[left], nums[right]])
                        
#                         # Skip duplicates for left pointer
#                         while left < right and nums[left] == nums[left + 1]:
#                             left += 1
#                         # Skip duplicates for right pointer
#                         while left < right and nums[right] == nums[right - 1]:
#                             right -= 1
                            
#                         left += 1
#                         right -= 1
#                     elif curr_sum < target:
#                         left += 1
#                     else:
#                         right -= 1   
#         return result