# 147. Insertion Sort List
# Medium

# Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.
# The steps of the insertion sort algorithm:
# Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
# It repeats until no input elements remain.
# The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.

# Example 1:
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]

# Example 2:
# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]

# Constraints:
# The number of nodes in the list is in the range [1, 5000].
# -5000 <= Node.val <= 5000


# sol 1

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head or not head.next:
#             return head
#         dummy = ListNode(0)
#         dummy.next = head
#         last_sorted = head
#         curr = head.next
#         while curr:
#             if last_sorted.val <= curr.val:
#                 last_sorted = last_sorted.next
#             else:
#                 prev = dummy
#                 while prev.next.val <= curr.val:
#                     prev = prev.next
#                 last_sorted.next = curr.next
#                 curr.next = prev.next
#                 prev.next = curr
#             curr = last_sorted.next
#         return dummy.next



# sol 2

# class Solution:
#     def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode()
#         curr = head
#         while curr:
#             prev = dummy
#             next_node = curr.next
#             while prev.next and prev.next.val < curr.val:
#                 prev = prev.next
#             curr.next = prev.next
#             prev.next = curr
#             curr = next_node
#         return dummy.next



# sol 3

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head==None or head.next==None:
#             return head
#         x=[]
#         temp=head
#         while temp!=None:
#             x.append(temp.val)
#             temp=temp.next
#         x.sort()
#         temp=head
#         for i in x:
#             temp.val=i
#             temp=temp.next
#         return head