# 2074. Reverse Nodes in Even Length Groups
# Medium

# You are given the head of a linked list.
# The nodes in the linked list are sequentially assigned to non-empty groups whose lengths form the sequence of the natural numbers (1, 2, 3, 4, ...). The length of a group is the number of nodes assigned to it. In other words,
# The 1st node is assigned to the first group.
# The 2nd and the 3rd nodes are assigned to the second group.
# The 4th, 5th, and 6th nodes are assigned to the third group, and so on.
# Note that the length of the last group may be less than or equal to 1 + the length of the second to last group.
# Reverse the nodes in each group with an even length, and return the head of the modified linked list.

# Example 1:
# Input: head = [5,2,6,3,9,1,7,3,8,4]
# Output: [5,6,2,3,9,1,4,8,3,7]
# Explanation:
# - The length of the first group is 1, which is odd, hence no reversal occurs.
# - The length of the second group is 2, which is even, hence the nodes are reversed.
# - The length of the third group is 3, which is odd, hence no reversal occurs.
# - The length of the last group is 4, which is even, hence the nodes are reversed.

# Example 2:
# Input: head = [1,1,0,6]
# Output: [1,0,1,6]
# Explanation:
# - The length of the first group is 1. No reversal occurs.
# - The length of the second group is 2. The nodes are reversed.
# - The length of the last group is 1. No reversal occurs.

# Example 3:
# Input: head = [1,1,0,6,5]
# Output: [1,0,1,5,6]
# Explanation:
# - The length of the first group is 1. No reversal occurs.
# - The length of the second group is 2. The nodes are reversed.
# - The length of the last group is 2. The nodes are reversed.

# Constraints:
# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 105



# sol 1

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         connector = None
#         curr = head
#         group_count = 1
#         count = 1

#         def reverse_between(pre, n):
#             start = pre.next
#             then = start.next
#             after = start

#             for _ in range(n - 1):
#                 start.next = then.next
#                 then.next = pre.next
#                 pre.next = then
#                 then = start.next

#             return after

#         while curr:
#             if group_count == count or not curr.next:
#                 if count % 2 == 0:
#                     curr = reverse_between(connector, count)
#                 connector = curr
#                 group_count += 1
#                 count = 0

#             count += 1
#             curr = curr.next

#         return head



# sol 2

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head or not head.next:
#             return head
#         max_steps = 1
#         prev = None
#         curr_node = head

#         while curr_node:
#             num_steps = 0

#             next_prev = None
#             next_start = curr_node
#             while num_steps < max_steps and next_start:
#                 next_prev = next_start
#                 next_start = next_start.next
#                 num_steps += 1
                
#             if num_steps % 2:
#                 curr_node = next_start
#                 prev = next_prev
#             else:
#                 new_prev = curr_node

#                 rev_prev = prev
#                 prev = next_start
#                 for iteration in range(num_steps):
#                     curr_node.next, prev, curr_node = prev, curr_node, curr_node.next
#                 rev_prev.next = prev

#                 prev = new_prev

#             max_steps += 1
#         return head

#         # if curr_move % 2:
#             #     while num_moves < curr_move and curr_node:
#             #         prev = curr_node
#             #         curr_node = curr_node.next
#             #         num_moves += 1
#             # else:
#             #     rev_head = prev

#             #     rev_tail = curr_node
#             #     prev = None
#             #     while num_moves < curr_move and rev_tail:
#             #         prev = rev_tail
#             #         rev_tail = rev_tail.next
#             #         num_moves += 1
                
#             #     if num_moves == curr_move:
#             #         rev_head.next = prev
#             #         prev = rev_tail
#             #         for iteration in range(curr_move):
#             #             temp = curr_node.next
#             #             curr_node.next = prev
#             #             prev = curr_node
#             #             curr_node = temp
                    
#             #     else:
#             #         curr_node = None