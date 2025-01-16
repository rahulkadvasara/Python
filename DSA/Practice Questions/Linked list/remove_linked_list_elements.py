# 203. Remove Linked List Elements
# Easy

# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Example 1:
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]

# Example 2:
# Input: head = [], val = 1
# Output: []

# Example 3:
# Input: head = [7,7,7,7], val = 7
# Output: []

# Constraints:
# The number of nodes in the list is in the range [0, 104].
# 1 <= Node.val <= 50
# 0 <= val <= 50




# sol 1

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
#         dummy=ListNode(0)
#         dummy.next=head 
#         curr=dummy
#         while curr.next:
#             if curr.next.val==val:
#                 curr.next=curr.next.next
#             else:
#                 curr=curr.next
#         return dummy.next
        


# sol 2

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
#         while head and head.val == val:\\Check if head itself have val
#             temp = head
#             head = head.next
#             del temp

#         ptr = head
#         preptr = None

#         while ptr:
#             if ptr.val == val:
#                 if preptr:
#                     preptr.next = ptr.next
#                 temp = ptr
#                 ptr = ptr.next
#                 del temp
#             else:
#                 preptr = ptr
#                 ptr = ptr.next
#         return head



# sol 3

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
#         dummy=ListNode(next=head)
#         prev,curr = dummy, head

#         while curr:
#             nxt=curr.next

#             if curr.val==val:
#                 prev.next = nxt
#             else:
#                 prev=curr

#             curr=nxt
#         return dummy.next