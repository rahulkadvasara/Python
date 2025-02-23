# 2594. Minimum Time to Repair Cars
# Medium

# You are given an integer array ranks representing the ranks of some mechanics. ranksi is the rank of the ith mechanic. A mechanic with a rank r can repair n cars in r * n2 minutes.
# You are also given an integer cars representing the total number of cars waiting in the garage to be repaired.
# Return the minimum time taken to repair all the cars.
# Note: All the mechanics can repair the cars simultaneously.

# Example 1:
# Input: ranks = [4,2,3,1], cars = 10
# Output: 16
# Explanation: 
# - The first mechanic will repair two cars. The time required is 4 * 2 * 2 = 16 minutes.
# - The second mechanic will repair two cars. The time required is 2 * 2 * 2 = 8 minutes.
# - The third mechanic will repair two cars. The time required is 3 * 2 * 2 = 12 minutes.
# - The fourth mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
# It can be proved that the cars cannot be repaired in less than 16 minutes.​​​​​

# Example 2:
# Input: ranks = [5,1,8], cars = 6
# Output: 16
# Explanation: 
# - The first mechanic will repair one car. The time required is 5 * 1 * 1 = 5 minutes.
# - The second mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
# - The third mechanic will repair one car. The time required is 8 * 1 * 1 = 8 minutes.
# It can be proved that the cars cannot be repaired in less than 16 minutes.​​​​​

# Constraints:
# 1 <= ranks.length <= 105
# 1 <= ranks[i] <= 100
# 1 <= cars <= 106



# sol 1

# class Solution:
#     def repairCars(self, A: List[int], cars: int) -> int:
#         return bisect_left(range(10**14), cars, key=lambda x: sum(int(sqrt(x / a)) for a in A))



# sol 2

# class Solution:
#     def repairCars(self, ranks: List[int], cars: int) -> int:
        
#         def canFinish(time: int) -> bool:
#             finish = 0
#             for r in ranks:
#                 finish += floor(math.sqrt(time / r))
#                 if finish >= cars:
#                     return True
#             return False

#         lo, hi = 0, max(ranks) * cars * cars
#         while lo < hi:
#             time = lo + (hi - lo) // 2
#             if canFinish(time):
#                 hi = time
#             else:
#                 lo = time + 1
#         return lo



# sol 3

# class Solution:
#     def canRepair(self, ranks, val, cars):
#         repaired = 0
#         for rank in ranks:
#             car = int(math.sqrt(val//rank))
#             repaired+=car 
#         if val==16:
#             print(repaired)
#         return repaired>=cars
#     def repairCars(self, ranks: List[int], cars: int) -> int:
#         mintime, maxtime = 0, max(ranks)*cars*cars
#         final = 0
#         while mintime<=maxtime:
#             mid = (mintime+maxtime)//2
#             if self.canRepair(ranks, mid, cars):
#                 final = mid
#                 maxtime = mid-1
#             else:
#                 mintime = mid+1
#         return final
        


# sol 4

# class Solution:
#     def repairCars(self, ranks: List[int], cars: int) -> int:
#         n = len(ranks)
#         left = 0
#         right = 100 * ceil(cars / n)**2
#         ranks = Counter(ranks)

#         def f(x):
#             result = 0
#             for rank, v in ranks.items():
#                 result += v * int(sqrt(x / rank))
#             return result

#         while right - left != 1:
#             mid = (left + right) // 2
#             if f(mid) >= cars:
#                 right = mid
#             else:
#                 left = mid
#         return right