# 21. Merge Two Sorted Lists
# Easy

# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]
 
# Constraints:
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.



# sol 1

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode(0)
#         head = dummy
#         while list1 and list2:
#             if list1.val<list2.val:
#                 head.next=list1
#                 list1=list1.next
#             else:
#                 head.next=list2
#                 list2=list2.next
#             head=head.next
#         head.next=list1 or list2
#         return dummy.next
        



# sol 2

# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         if not list1:
#             return list2
#         if not list2:
#             return list1
#         if list1.val<list2.val:
#             list1.next=self.mergeTwoLists(list1.next,list2)
#             return list1
#         else:
#             list2.next=self.mergeTwoLists(list1,list2.next)
#             return list2