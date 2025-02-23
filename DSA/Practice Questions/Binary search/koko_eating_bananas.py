# 875. Koko Eating Bananas
# Medium

# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
# Return the minimum integer k such that she can eat all the bananas within h hours.

# Example 1:
# Input: piles = [3,6,7,11], h = 8
# Output: 4

# Example 2:
# Input: piles = [30,11,23,4,20], h = 5
# Output: 30

# Example 3:
# Input: piles = [30,11,23,4,20], h = 6
# Output: 23

# Constraints:
# 1 <= piles.length <= 104
# piles.length <= h <= 109
# 1 <= piles[i] <= 109



# sol 1

# class Solution:
#     def minEatingSpeed(self, piles: List[int], h: int) -> int:
#         def possible(K):
#             return sum((p-1)//K + 1 for p in piles) <= h
#         l, r = 1, max(piles)
#         while l < r:
#             m = (l+r)//2
#             if not possible(m):
#                 l = m+1
#             else:
#                 r = m

#         return l


# sol 2

# class Solution:
#     def minEatingSpeed(self, piles: List[int], h: int) -> int:
#         l, r = 1, max(piles)
        
#         while l <= r:
#             mid = (l + r) // 2
#             total_hours = sum((pile + mid - 1) // mid for pile in piles)
            
#             if total_hours > h:
#                 l = mid + 1
#             else:
#                 r = mid - 1
                
#         return l


# sol 3


# class Solution:
#     def minEatingSpeed(self, piles: List[int], h: int) -> int:
#         left = 1 
#         right = max(piles)
        
#         while left<=right:
#             mid = (left+right)//2
#             c = 0
#             for pile in piles:
#                 c-=pile//-mid
#             if c<=h:
#                 right=mid-1
#             else:
#                 left=mid+1        
#         return left
        
        