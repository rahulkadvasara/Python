# 2089. Find Target Indices After Sorting Array

# You are given a 0-indexed integer array nums and a target element target.

# A target index is an index i such that nums[i] == target.

# Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

 

# Example 1:

# Input: nums = [1,2,5,2,3], target = 2
# Output: [1,2]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The indices where nums[i] == 2 are 1 and 2.
# Example 2:

# Input: nums = [1,2,5,2,3], target = 3
# Output: [3]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The index where nums[i] == 3 is 3.
# Example 3:

# Input: nums = [1,2,5,2,3], target = 5
# Output: [4]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The index where nums[i] == 5 is 4.
 

# Constraints:

# 1 <= nums.length <= 100
# 1 <= nums[i], target <= 100

# sol 1
# linear search
# class Solution:
#     def targetIndices(self, nums: List[int], target: int) -> List[int]:
#         nums.sort()
#         op=[]
#         for i in range(len(nums)):
#             if(nums[i]==target):
#                 op.append(i)
#         return op

# sol 2
# class Solution:
#     def targetIndices(self, nums: List[int], target: int) -> List[int]:
#         nums.sort()
#         return [i for i in range(len(nums)) if nums[i] == target]

# sol 3
# class Solution:
#     def targetIndices(self, nums: List[int], target: int) -> List[int]:
#         nums.sort()
#         l,h=0,len(nums)-1
#         left=right=-1
#         while l<=h:
#             m=(l+h)//2
#             if nums[m]==target:
#                 left=m
#                 h=m-1
#             elif nums[m]>target:
#                 h=m-1
#             else:
#                 l=m+1
#         l,h=left,len(nums)-1
#         while l<=h: 
#             m=(l+h)//2
#             if nums[m]==target:
#                 right=m
#                 l=m+1
#             elif nums[m]>target:
#                 h=m-1
#             else:
#                 l=m+1
#         if left==-1:
#             return []
#         ans=range(left,right+1)
#         return ans
        
# sol 4
# class Solution:
#     def targetIndices(self, nums: List[int], target: int) -> List[int]:
#         # implementing counting sort
#         d = defaultdict(int)

#         for num in nums:
#             d[num] += 1

#         if target not in d:
#             return []

#         # bounding indices
#         start = sum([v for k, v in d.items() if k < target])
#         end = start + d[target]

#         return list(range(start, end))

# sol 5
# class Solution:
#     def targetIndices(self, nums: List[int], target: int) -> List[int]:
#         countEqual , countLess = 0 , 0
#         for num in nums:
#             if(num==target): countEqual += 1
#             if(num<target): countLess += 1
#         res = [x for x in range(countLess,countLess+countEqual)]
#         return res


# sol 4
# from bisect import bisect_left
# from typing import List

# class Solution:
#     def maximumCount(self, nums: List[int]) -> int:
#         # Calculate the number of elements equal or greater than 1 using binary search.
#         # bisect_left returns the leftmost place in the sorted list to insert the number 1
#         # Subtract this from the length of the array to find the count of elements >= 1
#         count_ones_or_more = len(nums) - bisect_left(nums, 1)

#         # Calculate the number of elements which are negative using binary search.
#         # bisect_left returns the leftmost place in the sorted list to insert number 0
#         # It gives us the number of negative numbers since the list is sorted.
#         count_negative = bisect_left(nums, 0)

#         # Return the maximum of the two counts calculated
#         return max(count_ones_or_more, count_negative)

# sol 5
# class Solution:
#     def maximumCount(self, nums: List[int]) -> int:
#         a = sum(x > 0 for x in nums)
#         b = sum(x < 0 for x in nums)
#         return max(a, b)

# sol 6
# using binary search
# O(log(n))
# class Solution:
#     def maximumCount(self, nums: List[int]) -> int:
#         def binary_search_first_non_negative(nums):
#             low, high = 0, len(nums) - 1
#             while low <= high:
#                 mid = (low + high) // 2
#                 if nums[mid] < 0:
#                     low = mid + 1
#                 else:
#                     high = mid - 1
#             return low

#         def binary_search_first_positive(nums):
#             low, high = 0, len(nums) - 1
#             while low <= high:
#                 mid = (low + high) // 2
#                 if nums[mid] <= 0:
#                     low = mid + 1
#                 else:
#                     high = mid - 1
#             return low

#         neg_count = binary_search_first_non_negative(nums)
#         pos_count = len(nums) - binary_search_first_positive(nums)
        
#         return max(neg_count, pos_count)


# sol 7
# using binary search
# O(log(n))

# def maximumCount(nums: List[int]) -> int:

#     if nums[0] > 0 and nums[-1] > 0:
#         return len(nums)
    
#     if nums[0] < 0 and nums[-1] < 0:
#         return len(nums)
    
#     left, right = 0, len(nums) - 1

#     pos = 0
#     neg = 0

#     while left <= right:

#         mid = (left + right) // 2
            
#         if nums[mid] < 0:
#             neg = mid + 1
#             left = mid + 1
        
#         elif nums[mid] > 0:
#             pos = len(nums) - mid
#             right = mid - 1
        
#         if nums[mid] == 0:
#             if nums[left] < 0:
#                 neg+=1
#             left+=1


#     return max(pos, neg)

# f = open('user.out', 'w')
# for case in map(loads, stdin):
#     f.write(f"{maximumCount(case)}\n")
# f.flush()
# exit(0)


# sol 8
# using binary search
# O(log(n))

# def maximumCount(nums: List[int]) -> int:
#     neg = 0
#     pos = 0
#     for i, v in enumerate(nums):
#         if v > 0:
#             pos = len(nums[i:])
#             if pos > neg:
#                 return pos
#             else:
#                 return neg
#         if v != 0:
#             neg += 1

#     return neg

# f = open('user.out', 'w')
# for case in map(loads, stdin):
#     f.write(f"{maximumCount(case)}\n")
# f.flush()
# exit(0)