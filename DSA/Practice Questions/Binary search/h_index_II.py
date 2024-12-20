# 275. H-Index II
# Medium

# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper and citations is sorted in ascending order, return the researcher's h-index.
# According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.
# You must write an algorithm that runs in logarithmic time.

# Example 1:
# Input: citations = [0,1,3,5,6]
# Output: 3
# Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had received 0, 1, 3, 5, 6 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

# Example 2:
# Input: citations = [1,2,100]
# Output: 2
 
# Constraints:
# n == citations.length
# 1 <= n <= 105
# 0 <= citations[i] <= 1000
# citations is sorted in ascending order.



# sol 1

# class Solution:
#     def hIndex(self, citations: List[int]) -> int:
#         max_citation = max(citations)
#         counts = [0] * (max_citation + 1)
#         for citation in citations:
#             counts[citation] += 1
#         total_papers = 0
#         for h in range(max_citation, -1, -1):
#             total_papers += counts[h]
#             if total_papers >= h:
#                 return h
#         return 0
    

# sol 2

# class Solution:
#     def hIndex(self, citations: list[int]) -> int:
#         n = len(citations)
#         l, r = 0, n - 1
#         while l <= r:
#             m = l + (r - l) // 2
#             if citations[m] < n - m:
#                 l = m + 1
#             else:
#                 r = m - 1
#         return n - l

# with open('user.out', 'w') as f:
#     inputs = map(loads, stdin)
#     s = Solution()
#     for input in inputs:
#         print(s.hIndex(input), file=f)
# exit(0)