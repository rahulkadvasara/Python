# 34. Find First and Last Position of Element in Sorted Array
# Solved
# Medium
# Topics
# Companies
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109

# # sol 1
# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
        
#         def binary_search(nums, target, is_searching_left):
#             left = 0
#             right = len(nums) - 1
#             idx = -1
            
#             while left <= right:
#                 mid = (left + right) // 2
                
#                 if nums[mid] > target:
#                     right = mid - 1
#                 elif nums[mid] < target:
#                     left = mid + 1
#                 else:
#                     idx = mid
#                     if is_searching_left:
#                         right = mid - 1
#                     else:
#                         left = mid + 1
            
#             return idx
        
#         left = binary_search(nums, target, True)
#         right = binary_search(nums, target, False)
        
#         return [left, right]
            
# # sol 2
# f = open("user.out", 'w')
# for nums, tar in zip(stdin, stdin):
#     if nums[1] == ']':
#         print("[-1,-1]", file=f)
#         continue
#     a = nums[1:-2].split(',')
#     tar = tar.rstrip()
#     t = int(tar)
#     i = bisect_left(a, True, key=lambda x: int(x) >= t)
#     if i == len(a) or a[i] != tar:
#         print("[-1,-1]", file=f)
#     else:
#         j = bisect_left(a, True, key=lambda x: int(x) > t)
#         print(f"[{i},{j-1}]", file=f)
# exit(0)

