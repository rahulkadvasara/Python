# 86. Partition List
# Medium

# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
# You should preserve the original relative order of the nodes in each of the two partitions.

# Example 1:
# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]

# Example 2:
# Input: head = [2,1], x = 2
# Output: [1,2]
 
# Constraints:
# The number of nodes in the list is in the range [0, 200].
# -100 <= Node.val <= 100
# -200 <= x <= 200

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next



# sol 1

# class Solution:
#     def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
#         if not head:
#             return None
        
#         dummy = ListNode(next=head)
#         prev = dummy
#         curr = head
#         partition = None
        
#         while curr:
#             if curr.val < x:
#                 if partition:
#                     prev.next = curr.next
#                     curr.next = partition.next
#                     partition.next = curr
#                     partition = partition.next
#                     curr = prev.next
#                 else:
#                     prev = prev.next
#                     curr = curr.next
#             else:
#                 if not partition:
#                     partition = prev
#                 prev = prev.next
#                 curr = curr.next
        
#         return dummy.next



# sol 2

# class Solution:
#     def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
#         dummy1 = ListNode()
#         dummy2 = ListNode()
#         curr1 = dummy1
#         curr2 = dummy2
#         while head:
#             if head.val < x:
#                 curr1.next = head
#                 curr1 = curr1.next
#             else:
#                 curr2.next = head
#                 curr2 = curr2.next
#             head = head.next
#         curr2.next = None
#         curr1.next = dummy2.next
#         return dummy1.next



# sol 3

# class Solution:
#     def partition(self, head: ListNode, x: int) -> ListNode:
#         if not head:
#             return None
        
#         dummy = ListNode(next=head)
#         prev = dummy
#         curr = head
        
#         while curr:
#             if curr.val < x:
#                 prev = prev.next
#             else:
#                 break
#             curr = curr.next
        
#         while curr:
#             if curr.val < x:
#                 prev.next = curr.next
#                 curr.next = prev.next
#                 prev = prev.next
#             curr = curr.next
        
#         return dummy.next