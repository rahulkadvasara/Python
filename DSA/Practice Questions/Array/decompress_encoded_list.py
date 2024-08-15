# 1313. Decompress Run-Length Encoded List
# Easy
# Topics
# Companies
# Hint
# We are given a list nums of integers representing a list compressed with run-length encoding.

# Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, there are freq elements with value val concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.

# Return the decompressed list.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [2,4,4,4]
# Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
# The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
# At the end the concatenation [2] + [4,4,4] is [2,4,4,4].
# Example 2:

# Input: nums = [1,1,2,3]
# Output: [1,3,3]
 

# Constraints:

# 2 <= nums.length <= 100
# nums.length % 2 == 0
# 1 <= nums[i] <= 100


# sol 1
# class Solution:
#     def decompressRLElist(self, nums: List[int]) -> List[int]:
#         # freq=0
#         # val=0
#         op=[]
#         for i in range(len(nums)):
#             if i<len(nums)/2:
#                 freq=nums[2*i]
#                 val=nums[(2*i)+1]
#                 for j in range(freq):
#                     op.append(val)
#         return op
            

# sol 2
# class Solution:
#     def decompressRLElist(self, nums: List[int]) -> List[int]:
#         return reduce(
#             lambda x, y: x + y,
#             (f * [v] for f, v in list(zip(*([iter(nums)] * 2)))),
#         )

# sol 3
# class Solution:
#     def decompressRLElist(self, nums: List[int]) -> List[int]:
#         res = []
#         n = len(nums)
#         i = 0

#         while i < n :
#             val = nums[i + 1]
#             freq = nums[i]
#             res.extend([val] * freq)
#             i += 2
#         return res


