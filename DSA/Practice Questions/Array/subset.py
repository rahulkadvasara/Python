# 78. Subsets
# Medium

# Given an integer array nums of unique elements, return all possible 
# subsets
#  (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Example 2:
# Input: nums = [0]
# Output: [[],[0]]

# Constraints:
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.



# solution

# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         n=len(nums)
#         res=[]
#         sol=[]

#         def backtrack(i):
#             if(i==n):
#                 res.append(sol[:])
#                 return
            
#             # Don't pick nums[i]
#             backtrack(i+1)

#             # Pick nums[i]
#             sol.append(nums[i])
#             backtrack(i+1)
#             sol.pop()
        
#         backtrack(0)
#         return res