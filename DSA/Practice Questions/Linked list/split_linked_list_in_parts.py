# 725. Split Linked List in Parts
# Medium

# Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.
# The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.
# The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.
# Return an array of the k parts.

# Example 1:
# Input: head = [1,2,3], k = 5
# Output: [[1],[2],[3],[],[]]
# Explanation:
# The first element output[0] has output[0].val = 1, output[0].next = null.
# The last element output[4] is null, but its string representation as a ListNode is [].

# Example 2:
# Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
# Output: [[1,2,3,4],[5,6,7],[8,9,10]]
# Explanation:
# The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.

# Constraints:
# The number of nodes in the list is in the range [0, 1000].
# 0 <= Node.val <= 1000
# 1 <= k <= 50



# sol 1

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
#         n = 0
#         cur = head
#         while cur:
#             n += 1
#             cur = cur.next
#         width, remainder = divmod(n, k)
        
#         parts = []
#         cur = head
#         for i in range(k):
#             head = cur
#             for j in range(width + (i < remainder) - 1):
#                 if cur:
#                     cur = cur.next
#             if cur:
#                 cur.next, cur = None, cur.next
#             parts.append(head)
#         return parts



# sol 2

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
#         current = head
#         count = 0
#         while current:
#             count += 1
#             current = current.next
        
#         # Step 2: Calculate the size of each part and the number of extra nodes
#         part_size, extra_nodes = divmod(count, k)
        
#         # Step 3: Split the list into k parts
#         current = head
#         result = []
#         for i in range(k):
#             part_head = current
#             for j in range(part_size - 1 + (i < extra_nodes)):
#                 if current:
#                     current = current.next
#             if current:
#                 next_node = current.next
#                 current.next = None
#                 current = next_node
#             result.append(part_head)
        
#         return result