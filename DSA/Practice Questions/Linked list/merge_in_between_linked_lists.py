# 1669. Merge In Between Linked Lists
# Medium

# You are given two linked lists: list1 and list2 of sizes n and m respectively.
# Remove list1's nodes from the ath node to the bth node, and put list2 in their place.
# The blue edges and nodes in the following figure indicate the result:
# Build the result list and return its head.

# Example 1:
# Input: list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
# Output: [10,1,13,1000000,1000001,1000002,5]
# Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.

# Example 2:
# Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
# Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
# Explanation: The blue edges and nodes in the above figure indicate the result.
 
# Constraints:
# 3 <= list1.length <= 104
# 1 <= a <= b < list1.length - 1
# 1 <= list2.length <= 104



# sol 1

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
#         dummy = ListNode(next=list1)
#         prev = dummy
#         for i in range(a):
#             prev = prev.next
#         cur = prev
#         for i in range(b-a+1):
#             cur = cur.next
#         prev.next = list2
#         while prev.next:
#             prev = prev.next
#         prev.next = cur.next
#         return dummy.next



# sol 2

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
#         dummy = ListNode(next=list1)
#         cur = dummy
#         for _ in range(a):
#             cur = cur.next
#         start = cur
#         for _ in range(b-a+1):
#             cur = cur.next
#         end = cur.next
#         start.next = list2
#         while list2.next:
#             list2 = list2.next
#         list2.next = end
#         return dummy.next


# sol 3

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
#         dummy = ListNode(next=list1)
#         curr = dummy
#         for _ in range(a):
#             curr = curr.next
#         temp = curr
#         for _ in range(b-a+1):
#             temp = temp.next
#         curr.next = list2
#         while curr.next:
#             curr = curr.next
#         curr.next = temp.next
#         return dummy.next



# sol 4

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
#         # Create a dummy node to simplify edge cases
#         dummy = ListNode(0)
#         dummy.next = list1

#         # Step 1: Move preA to the (a-1)-th node
#         preA = dummy
#         for _ in range(a):
#             preA = preA.next

#         # Step 2: Move postB to the b-th node (starting from preA)
#         # after these moves, postB should be at the b-th node
#         postB = preA
#         for _ in range(b - a + 1):
#             postB = postB.next

#         # The node after postB is the (b+1)-th node
#         b_plus_1 = postB.next

#         # Step 3: Link preA.next to list2
#         preA.next = list2

#         # Step 4: Find the tail of list2
#         tail = list2
#         while tail.next:
#             tail = tail.next

#         # Step 5: Link the tail of list2 to b_plus_1
#         tail.next = b_plus_1

#         # Return the head of the modified list
#         return list1


