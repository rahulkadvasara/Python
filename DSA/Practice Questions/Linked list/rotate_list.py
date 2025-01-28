# 61. Rotate List
# Medium

# Given the head of a linked list, rotate the list to the right by k places.

# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

# Example 2:
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
 
# Constraints:
# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109



# sol 1

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         if not head:
#             return None
#         if not head.next:
#             return head
#         if k == 0:
#             return head
#         length = 1
#         last = head
#         while last.next:
#             last = last.next
#             length += 1
#         k = k % length
#         if k == 0:
#             return head
#         last.next = head
#         for _ in range(length - k):
#             last = last.next
#         head = last.next
#         last.next = None
#         return head


# sol 2

# class Solution:
#     def rotateRight(self, head: ListNode, k: int) -> ListNode:
#         if not head:
#             return None
#         if not head.next:
#             return head
#         n = 1
#         cur = head
#         while cur.next:
#             cur = cur.next
#             n += 1
#         cur.next = head
#         k = k % n
#         for _ in range(n - k):
#             cur = cur.next
#         head = cur.next
#         cur.next = None
#         return head


# sol 3

# class Solution:
#     def rotateRight(self, head: ListNode, k: int) -> ListNode:
#         if not head or not head.next or k == 0:
#             return head
        
#         # find the length of the linked list
#         length = 1
#         last = head
#         while last.next:
#             last = last.next
#             length += 1
        
#         # if k is a multiple of length, the list will be the same
#         if k % length == 0:
#             return head
        
#         # find the new head
#         new_head = head
#         for _ in range(length - k % length - 1):
#             new_head = new_head.next
        
#         # rotate the list
#         last.next = head
#         head = new_head.next
#         new_head.next = None
        
#         return head