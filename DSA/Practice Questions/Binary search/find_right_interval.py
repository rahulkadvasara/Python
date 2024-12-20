# 436. Find Right Interval
# Medium

# You are given an array of intervals, where intervals[i] = [starti, endi] and each starti is unique.
# The right interval for an interval i is an interval j such that startj >= endi and startj is minimized. Note that i may equal j.
# Return an array of right interval indices for each interval i. If no right interval exists for interval i, then put -1 at index i.

# Example 1:
# Input: intervals = [[1,2]]
# Output: [-1]
# Explanation: There is only one interval in the collection, so it outputs -1.

# Example 2:
# Input: intervals = [[3,4],[2,3],[1,2]]
# Output: [-1,0,1]
# Explanation: There is no right interval for [3,4].
# The right interval for [2,3] is [3,4] since start0 = 3 is the smallest start that is >= end1 = 3.
# The right interval for [1,2] is [2,3] since start1 = 2 is the smallest start that is >= end2 = 2.

# Example 3:
# Input: intervals = [[1,4],[2,3],[3,4]]
# Output: [-1,2,-1]
# Explanation: There is no right interval for [1,4] and [3,4].
# The right interval for [2,3] is [3,4] since start2 = 3 is the smallest start that is >= end1 = 3.
 
# Constraints:
# 1 <= intervals.length <= 2 * 104
# intervals[i].length == 2
# -106 <= starti <= endi <= 106
# The start point of each interval is unique.



# sol 1

# class Solution:
#     def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
#         first = sorted([ [arr[0], i] for i,arr in enumerate(intervals) ]) + [[float('inf'), -1]]
#         return [ first[ bisect_left(first, [arr[1]] )][1] for arr in intervals ]
    

# sol 2

# class Solution:
#     def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
#         mapping={}
#         for idx, interval in enumerate(intervals):
#             mapping[interval[0]]=idx
#         print(mapping)
#         intervals.sort()
#         n=len(intervals)
#         def binary_search(intervals, target):
#             left=0
#             right=n-1
#             while left <= right:
#                 mid = left + (right-left)//2
#                 if intervals[mid][0] < target:
#                     left = mid + 1
#                 else:
#                     right = mid - 1
#             if left == n:
#                 return -1
#             else:
#                 return left
#         res = [-1] * n
#         for i in range(n):
#             idx2 = binary_search(intervals, intervals[i][1])
#             if idx2 != -1:
#                 res[mapping[intervals[i][0]]] = mapping[intervals[idx2][0]]
#             else:
#                 res[mapping[intervals[i][0]]] = -1
#         return res