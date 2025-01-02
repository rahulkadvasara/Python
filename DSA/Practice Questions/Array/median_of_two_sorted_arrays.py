# 4. Median of Two Sorted Arrays
# Hard

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

# Constraints:
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106



# sol 1

# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         m=len(nums1)
#         n=len(nums2)
#         mid=(m+n)//2
#         arr=nums1+nums2
#         arr.sort()
#         op=0
#         if((m+n)%2==0):
#             op=(arr[mid-1]+arr[mid])/2
#         else:
#             op = arr[mid]
#         return op
        

# sol 2

# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2):
#         merged = nums1 + nums2
#         merged.sort()
#         total = len(merged)

#         if total % 2 == 1:
#             return float(merged[total // 2])
#         else:
#             middle1 = merged[total // 2 - 1]
#             middle2 = merged[total // 2]
#             return (float(middle1) + float(middle2)) / 2.0
        

# sol 3

# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2):
#         n = len(nums1)
#         m = len(nums2)
#         i,j,m1,m2 = 0,0,0,0
#         for count in range(0, (n + m) // 2 + 1):
#             m2 = m1
#             if i < n and j < m:
#                 if nums1[i] > nums2[j]:
#                     m1 = nums2[j]
#                     j += 1
#                 else:
#                     m1 = nums1[i]
#                     i += 1
#             elif i < n:
#                 m1 = nums1[i]
#                 i += 1
#             else:
#                 m1 = nums2[j]
#                 j += 1
#         if (n + m) % 2 == 1:
#             return float(m1)
#         else:
#             ans = float(m1) + float(m2)
#             return ans / 2.0
        


# sol 4

# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2):
#         n1 = len(nums1)
#         n2 = len(nums2)
        
#         if n1 > n2:
#             return self.findMedianSortedArrays(nums2, nums1)
#         n = n1 + n2
#         left = (n1 + n2 + 1) // 2 
#         low = 0
#         high = n1
        
#         while low <= high:
#             mid1 = (low + high) // 2 
#             mid2 = left - mid1 
            
#             l1 = float('-inf')
#             l2 = float('-inf')
#             r1 = float('inf')
#             r2 = float('inf')

#             if mid1 < n1:
#                 r1 = nums1[mid1]
#             if mid2 < n2:
#                 r2 = nums2[mid2]
#             if mid1 - 1 >= 0:
#                 l1 = nums1[mid1 - 1]
#             if mid2 - 1 >= 0:
#                 l2 = nums2[mid2 - 1]
            
#             if l1 <= r2 and l2 <= r1:
#                 if n % 2 == 1:
#                     return max(l1, l2)
#                 else:
#                     return (max(l1, l2) + min(r1, r2)) / 2.0
#             elif l1 > r2:
#                 high = mid1 - 1
#             else:
#                 low = mid1 + 1
        
#         return 0
    


# sol 5

# import numpy as np
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         c = nums1+nums2
#         return np.median(c)
    


# sol 6

# class Solution:     
#     def findMedianSortedArrays(self, a, b):
#         l = len(a) + len(b)
#         if l % 2:
#             return self.get_median(a, b, l // 2)
#         else:
#             return (self.get_median(a, b, l // 2) + self.get_median(a, b, l // 2 - 1))  / 2

#     def get_median(self, a, b, idx):
#         if not a:
#             return b[idx]
#         if not b:
#             return a[idx]

#         ai = len(a) // 2
#         bi = len(b) // 2
#         ma = a[ai]
#         mb = b[bi]

#         if ma > mb:
#             ma, mb = mb, ma
#             ai, bi = bi, ai
#             a, b = b, a

#         max_idx_ma = len(a) // 2 + len(b) // 2

#         if max_idx_ma < idx:
#             med = self.get_median(a[ai+1:], b, idx - (len(a)//2+1))
#         else:
#             med = self.get_median(a, b[:bi], idx)

#         return med