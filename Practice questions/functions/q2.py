# star pattern
# *
# * *
# * * *

n = int(input("Enter a number: "))

# for i in range(n):
#         s = ''
#         for j in range(i+1):
#             s = s + '*'
#         print(s)

# for i in range(1, n+1):
#     for k in range(1, i+1):
#         print("*", end="")
#     print()

for i in range(1, n+1):
    print("*" * i)