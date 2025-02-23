# 25. Reverse Nodes in k-Group
# Hard

# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# You may not alter the values in the list's nodes, only nodes themselves may be changed.

# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]

# Example 2:
# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]

# Constraints:
# The number of nodes in the list is n.
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000

# Follow-up: Can you solve the problem in O(1) extra memory space?



# sol 1

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
#         if not head or k == 1:
#             return head

#         dummy = ListNode(0)
#         dummy.next = head
#         prev = dummy
#         curr = head

#         # Count the number of nodes in the list
#         count = 0
#         while curr:
#             count += 1
#             curr = curr.next

#         # Reverse k nodes at a time
#         while count >= k:
#             curr = prev.next
#             nxt = curr.next

#             # Reverse k nodes
#             for _ in range(1, k):
#                 curr.next = nxt.next
#                 nxt.next = prev.next
#                 prev.next = nxt
#                 nxt = curr.next

#             prev = curr
#             count -= k

#         return dummy.next



# sol 2

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         dummy = ListNode()
#         dummy.next = head

#         prev = dummy
#         curr = head

#         while True:
#             nodesCountK = True

#             for i in range(k):
#                 if curr:
#                     curr = curr.next
#                 else:
#                     nodesCountK = False
#                     break

#             if not nodesCountK:
#                 break

#             curr = prev.next

#             for i in range(k - 1):
#                 next = curr.next

#                 curr.next = next.next
#                 next.next = prev.next
#                 prev.next = next
                

#             prev = curr
#             curr = prev.next
        
#         return dummy.next