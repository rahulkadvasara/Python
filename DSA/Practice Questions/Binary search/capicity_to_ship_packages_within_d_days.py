# 1011. Capacity To Ship Packages Within D Days
# Medium

# A conveyor belt has packages that must be shipped from one port to another within days days.
# The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.
# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

# Example 1:
# Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
# Output: 15
# Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
# 1st day: 1, 2, 3, 4, 5
# 2nd day: 6, 7
# 3rd day: 8
# 4th day: 9
# 5th day: 10
# Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.

# Example 2:
# Input: weights = [3,2,2,4,1,4], days = 3
# Output: 6
# Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
# 1st day: 3, 2
# 2nd day: 2, 4
# 3rd day: 1, 4

# Example 3:
# Input: weights = [1,2,3,1,1], days = 4
# Output: 3
# Explanation:
# 1st day: 1
# 2nd day: 2
# 3rd day: 3
# 4th day: 1, 1

# Constraints:
# 1 <= days <= weights.length <= 5 * 104
# 1 <= weights[i] <= 500



# sol 1

# class Solution:
#     def shipWithinDays(self, weights: List[int], days: int) -> int:
#         def canShip(capacity):
#             total = 0
#             required_days = 1
#             for weight in weights:
#                 if total + weight > capacity:
#                     required_days += 1
#                     total = 0
#                 total += weight
#             return required_days <= days

#         left, right = max(weights), sum(weights)
#         while left < right:
#             mid = (left + right) // 2
#             if canShip(mid):
#                 right = mid
#             else:
#                 left = mid + 1
#         return left



# sol 2

# class Solution:
#     def shipWithinDays(self, weights: List[int], days: int) -> int:
#         maxWeight, totalWeight = -1, 0
#         for weight in weights:
#             maxWeight = max(maxWeight, weight)
#             totalWeight += weight
#         left, right = maxWeight, totalWeight
#         while left < right:
#             mid = (left + right) // 2
#             daysNeeded, currWeight = 1, 0
#             for weight in weights:
#                 if currWeight + weight > mid:
#                     daysNeeded += 1
#                     currWeight = 0
#                 currWeight += weight
#             if daysNeeded > days:
#                 left = mid + 1
#             else:
#                 right = mid
#         return left


    
# sol 3

# class Solution:
#     def shipWithinDays(self, W: List[int], days: int) -> int:
#         def can_ship(capacity):
#             curTotal = 0
#             daysNeeded = 1
#             for weight in W:           
#                 curTotal += weight 
#                 if curTotal > capacity: 
#                 #ship current load- wait a day to ship more 
#                     curTotal = weight
#                     daysNeeded += 1
#             return daysNeeded <= days

#         '''Binary search for capacity'''
#         maxW= max(W) 
#         l = max(ceil(sum(W)/days), maxW)
#         r = min(l + maxW, ceil(len(W) / days) * maxW)
#         # r = l + maxW # also works almost the same. 
#         while l < r:
#             mid = (l+r)//2 
#             curTotal = 0
#             daysNeeded = 1
#             for weight in W:           
#                 curTotal += weight 
#                 if curTotal > mid: 
#                 #ship current load- wait a day to ship more 
#                     curTotal = weight
#                     daysNeeded += 1
#             if daysNeeded <= days: #capacity is sufficient- see if smaller capacities work
#                 r = mid
#             else: #capacity is too high- reduce search space to higher capacities
#                 l = mid + 1
#         return l 
        



# sol 4

# class Solution:
#     def shipWithinDays(self, weights: List[int], days: int) -> int:
#         def canShip(capacity):
#             total = 0
#             required_days = 1
#             for weight in weights:
#                 if total + weight > capacity:
#                     required_days += 1
#                     total = 0
#                 total += weight
#             return required_days <= days

#         left, right = max(weights), sum(weights)
#         while left < right:
#             mid = (left + right) // 2
#             if canShip(mid):
#                 right = mid
#             else:
#                 left = mid + 1
#         return left