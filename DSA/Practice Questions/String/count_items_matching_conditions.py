# 1773. Count Items Matching a Rule
# Easy
# Topics
# Companies
# Hint
# You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.

# The ith item is said to match the rule if one of the following is true:

# ruleKey == "type" and ruleValue == typei.
# ruleKey == "color" and ruleValue == colori.
# ruleKey == "name" and ruleValue == namei.
# Return the number of items that match the given rule.

 

# Example 1:

# Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"
# Output: 1
# Explanation: There is only one item matching the given rule, which is ["computer","silver","lenovo"].
# Example 2:

# Input: items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"
# Output: 2
# Explanation: There are only two items matching the given rule, which are ["phone","blue","pixel"] and ["phone","gold","iphone"]. Note that the item ["computer","silver","phone"] does not match.
 

# Constraints:

# 1 <= items.length <= 104
# 1 <= typei.length, colori.length, namei.length, ruleValue.length <= 10
# ruleKey is equal to either "type", "color", or "name".
# All strings consist only of lowercase letters.


# sol 1
# class Solution:
#     def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
#         op=0
#         for i in range(len(items)):
#                 if (ruleKey=="type" and ruleValue==items[i][0]) or (ruleKey=="color" and ruleValue==items[i][1]) or (ruleKey=="name" and ruleValue==items[i][2]):
#                     op+=1                    
#         return op

# sol 2
# class Solution:
#     def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
#         return sum([1 for i in range(len(items)) if (ruleKey=="type" and ruleValue==items[i][0]) or (ruleKey=="color" and ruleValue==items[i][1]) or (ruleKey=="name" and ruleValue==items[i][2])])

# sol 3
# class Solution:
#     def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
#         if(ruleKey=='type'):
#             k=0
#         elif(ruleKey=='color'):
#             k=1
#         else:
#             k=2
#         c=0
#         for i in items:
#             if(i[k]==ruleValue):
#                 c+=1
#         return c

# sol 4
# class Solution:
#     def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
#         d = {'type': 0, 'color': 1, 'name': 2}
#         return sum(1 for item in items if item[d[ruleKey]] == ruleValue)

# sol 5
# class Solution:
#     def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
#         return sum(1 for t, c, n in items if (ruleKey, ruleValue) in (("type", t), ("color", c), ("name", n)))

