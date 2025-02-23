# 1482. Minimum Number of Days to Make m Bouquets
# Medium

# You are given an integer array bloomDay, an integer m and an integer k.
# You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.
# The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.
# Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.

# Example 1:
# Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
# Output: 3
# Explanation: Let us see what happened in the first three days. x means flower bloomed and _ means flower did not bloom in the garden.
# We need 3 bouquets each should contain 1 flower.
# After day 1: [x, _, _, _, _]   // we can only make one bouquet.
# After day 2: [x, _, _, _, x]   // we can only make two bouquets.
# After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.

# Example 2:
# Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
# Output: -1
# Explanation: We need 3 bouquets each has 2 flowers, that means we need 6 flowers. We only have 5 flowers so it is impossible to get the needed bouquets and we return -1.

# Example 3:
# Input: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
# Output: 12
# Explanation: We need 2 bouquets each should have 3 flowers.
# Here is the garden after the 7 and 12 days:
# After day 7: [x, x, x, x, _, x, x]
# We can make one bouquet of the first three flowers that bloomed. We cannot make another bouquet from the last three flowers that bloomed because they are not adjacent.
# After day 12: [x, x, x, x, x, x, x]
# It is obvious that we can make two bouquets in different ways.


# Constraints:
# bloomDay.length == n
# 1 <= n <= 105
# 1 <= bloomDay[i] <= 109
# 1 <= m <= 106
# 1 <= k <= n



# sol 1

# class Solution:
#     def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
#         l, r = 1, 1000000000
#         ans = -1
#         while l <= r:
#             mid = l + (r - l) // 2
#             consecutive_length, bouquets = 0, 0
#             for bloom in bloomDay:
#                 if bloom <= mid:
#                     consecutive_length += 1
#                     if consecutive_length >= k:
#                         consecutive_length = 0
#                         bouquets += 1
#                 else:
#                     consecutive_length = 0
#             if bouquets >= m:
#                 ans = mid
#                 r = mid - 1
#             else:
#                 l = mid + 1
#         return ans



# sol 2

# class Solution:
#     def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
#         n = len(bloomDay)
#         if m * k > n:
#             return -1

#         if m * k == 1:
#             return min(bloomDay)

#         def modify(move,index):
#             if not move:
#                 move.append(index)
#                 return index // k + (n - index - 1) // k - n // k
#             loc = bisect_left(move,index)
#             left = -1 if loc == 0 else move[loc-1]
#             right = n if loc == len(move) else move[loc]
#             move.insert(loc,index)
#             return (index - left - 1) // k + (right - index - 1) // k - (right - left - 1) // k

#         bloom = [(-v,i) for i, v in enumerate(bloomDay)]
#         heapq.heapify(bloom)

#         move = []
#         total = n // k

#         for i in range(n - m * k):
#             value, index = heapq.heappop(bloom)
#             now = modify(move,index)
#             total += now
            
#             if total < m:
#                 return -value

#         return -heapq.heappop(bloom)[0]



# sol 3

# class Solution:
#     def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

#         def possible(bloomDay,day,m,k):
#             cnt=0
#             b_count=0
#             for i in bloomDay:
#                 if i<=day:
#                     cnt+=1
#                 else:
#                     b_count+=cnt//k
#                     cnt=0
#             b_count+=cnt//k
#             return b_count>=m
        
#         l=min(bloomDay)
#         r=max(bloomDay)
#         ans=-1
#         if len(bloomDay)<(m*k):
#             return -1
#         while l<=r:
#             mid=(l+r)//2
#             if possible(bloomDay,mid,m,k):
#                 ans=mid
#                 r=mid-1
#             else:
#                 l=mid+1
#         return ans

#         #for day in range(min_day,max_day+1):
#           #  if possible(bloomDay,day,m,k):
#          #       return day
#         #return -1
        