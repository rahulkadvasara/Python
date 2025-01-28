# 82. Remove Duplicates from Sorted List II
# Medium

# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

# Example 1:
# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]

# Example 2:
# Input: head = [1,1,1,2,3]
# Output: [2,3]

# Constraints:
# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.



# sol 1

# class Solution:
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         if not head:
#             return None
        
#         dummy = ListNode(next=head)
#         prev = dummy
#         curr = head
        
#         while curr:
#             if curr.next and curr.val == curr.next.val:
#                 while curr.next and curr.val == curr.next.val:
#                     curr = curr.next
#                 prev.next = curr.next
#             else:
#                 prev = prev.next
#             curr = curr.next
        
#         return dummy.next



# sol 2

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode(next=head)
#         prev = dummy
#         while head:
#             if head.next and head.val == head.next.val:
#                 while head.next and head.val == head.next.val:
#                     head = head.next
#                 prev.next = head.next
#             else:
#                 prev = prev.next
#             head = head.next
#         return dummy.next