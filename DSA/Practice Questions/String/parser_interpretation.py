# 1678. Goal Parser Interpretation

# You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

# Given the string command, return the Goal Parser's interpretation of command.

 

# Example 1:

# Input: command = "G()(al)"
# Output: "Goal"
# Explanation: The Goal Parser interprets the command as follows:
# G -> G
# () -> o
# (al) -> al
# The final concatenated result is "Goal".
# Example 2:

# Input: command = "G()()()()(al)"
# Output: "Gooooal"
# Example 3:

# Input: command = "(al)G(al)()()G"
# Output: "alGalooG"
 

# Constraints:

# 1 <= command.length <= 100
# command consists of "G", "()", and/or "(al)" in some order.

# sol 1
# class Solution:
#     def interpret(self, command: str) -> str:
#         if len(command) == "": return ""
#         new_input = ""
#         next = 0
#         for i in range(len(command)):
#             if command[i] == "G": new_input += command[i]
#             if command[i] == "(" and command[next + 1] == ")": new_input += "o"
#             if command[i] == "(" and command[next + 1] == "a": new_input += "al"
#             next += 1
#         return new_input

# sol 2
# class Solution:
#     def interpret(self, command: str) -> str:
#         return command.replace("()","o").replace("(al)","al")

# sol 3
# class Solution:
#     def interpret(self, command: str) -> str:
#         res=[]
#         for i in range(len(command)):
#             if command[i]=="G":
#                 res.append("G")
#             elif command[i]=="(":
#                 if command[i+1]==")":
#                     res.append("o")
#                 elif command[i+1]=="a":
#                     res.append("al")
#         return "".join(res)