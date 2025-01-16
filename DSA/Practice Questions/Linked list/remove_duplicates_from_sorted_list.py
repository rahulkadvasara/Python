# 83. Remove Duplicates from Sorted List
# Easy

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Example 1:
# Input: head = [1,1,2]
# Output: [1,2]

# Example 2:
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
 
# Constraints:
# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.



# sol 1

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         if not head:
#             return head
#         current = head
#         while current.next:
#             if current.val == current.next.val:
#                 current.next = current.next.next
#             else:
#                 current = current.next
#         return head



# sol 2

# class Solution:
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         if not head:
#             return head
#         current = head
#         while current:
#             while current.next and current.val == current.next.val:
#                 current.next = current.next.next
#             current = current.next
#         return head



# sol 3

# class Solution:
#     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         res = head

#         while head and head.next:
#             if head.val == head.next.val:
#                 head.next = head.next.next
#             else:
#                 head = head.next
        
#         return res



# sol 4

# class Solution:
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         current = head
#         while current is not None and current.next is not None:
#             if current.next.val == current.val:
#                 current.next = current.next.next
#             else:
#                 current = current.next
#         return head