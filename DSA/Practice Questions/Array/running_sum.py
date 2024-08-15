# 1480. Running Sum of 1d Array
# Easy
# Topics
# Companies
# Hint
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
# Example 2:

# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
# Example 3:

# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]
 

# Constraints:

# 1 <= nums.length <= 1000
# -10^6 <= nums[i] <= 10^6


# sol 1
# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         op=[]
#         for i in range(len(nums)):
#             if i==0:
#                 op.append(nums[0])
#             else:
#                 op.append(op[i-1]+nums[i])
#         return op

# sol 2
# def runningSum(self, nums: List[int]) -> List[int]:
# 	answer = [] #array to keep track of our answer
# 	for i in range(len(nums)): #iterate through all the elements in nums
# 		runningSum = 0 #this will keep track of the running sum up to index i
# 		for j in range(i+1): 
# 			runningSum += nums[j] #sum all the elements leading up to nums[i]
# 		answer.append(runningSum) #add the sum to our answer array
# 	return answer

# sol 3
# def runningSum(self, nums: List[int]) -> List[int]:
#    return [sum(nums[:i+1]) for i in range(len(nums))]

# sol 4
# def runningSum(self, nums: List[int]) -> List[int]:
# 	runSum = [nums[0]] #our answer array starts with nums[0], which is the 0th running sum
# 	for i in range(1,len(nums)):
# 		runSum.append(runSum[i-1]+nums[i]) #the running sum up to index i is the sum of nums[i] and the running sum up to index i-1
# 	return runSum

# sol 5
# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         for i in range(1,len(nums)):
#             nums[i] = nums[i-1] + nums[i]
#         return nums

# sol 6
# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         # Create an output array of size equal to given nums size...
#         output = [0] * len(nums)
#         # Set output[0] = nums[0]...
#         output[0] = nums[0]
#         # Traverse all elements through the for loop...
#         for idx in range(1, len(nums)):
#             # Storing the running sum...
#             output[idx] = output[idx - 1] + nums[idx]
#         return output       # Return the running sum of nums...

# sol 7
# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         ans=[]
#         sum=0
#         for i in nums:
#             sum=sum+i
#             ans.append(sum)
#         return ans





