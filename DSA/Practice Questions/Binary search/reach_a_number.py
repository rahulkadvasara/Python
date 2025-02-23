# 754. Reach a Number
# Medium

# You are standing at position 0 on an infinite number line. There is a destination at position target.
# You can make some number of moves numMoves so that:
# On each move, you can either go left or right.
# During the ith move (starting from i == 1 to i == numMoves), you take i steps in the chosen direction.
# Given the integer target, return the minimum number of moves required (i.e., the minimum numMoves) to reach the destination.

# Example 1:
# Input: target = 2
# Output: 3
# Explanation:
# On the 1st move, we step from 0 to 1 (1 step).
# On the 2nd move, we step from 1 to -1 (2 steps).
# On the 3rd move, we step from -1 to 2 (3 steps).

# Example 2:
# Input: target = 3
# Output: 2
# Explanation:
# On the 1st move, we step from 0 to 1 (1 step).
# On the 2nd move, we step from 1 to 3 (2 steps).

# Constraints:
# -109 <= target <= 109
# target != 0



# sol 1

# class Solution:
# 	def reachNumber(self, target: int) -> int:
# 		queue = [0]
# 		step = 1

# 		while queue:
# 			curr_level = len(queue)
# 			for i in range(curr_level):
# 				current = queue.pop(0)
# 				go_left = current - step
# 				go_right = current + step
				
# 				if go_left == target or go_right == target:
# 					return step
				
# 				queue += [go_left, go_right]
# 			step += 1
		
# 		return -1



# sol 2

# class Solution:
#     def reachNumber(self, target: int) -> int:
#         target = abs(target)
#         step = total = 0

#         while total < target:
#             step += 1
#             total += step
        
#         while (total - target) % 2 != 0:
#             step += 1
#             total += step

#         return step
        

# sol 3

# class Solution:
# 	def reachNumber(self, target: int) -> int:
# 		target = abs(target)
# 		m = math.ceil((math.sqrt(1 + 8 * target) - 1) / 2)
# 		total = m * (m + 1) / 2
		
# 		if (total - target) % 2 == 0:
# 			return n
# 		return n + 2 if n % 2 == 1 else n + 1



# sol 4

# class Solution:
#     def reachNumber(self, target: int) -> int:
#         target = abs(target)
#         l = 1
#         r = 10**5

#         while l < r:
#             mid = (l+r)//2
#             max_num = (mid + 1) * mid / 2
#             print(f"l={l},r={r},mid={mid}, max_num={max_num}")
#             if max_num == target:
#                 return mid
#             if max_num > target:
#                 r = mid
#             else:
#                 l = mid + 1
        
#         while (l+1)*l/2 % 2 != target % 2:
#             l += 1
#         print(f"l={l}, r={r}")

#         return l