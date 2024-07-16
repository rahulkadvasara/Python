# # Globle defination in a function
# x=20
# def func():
#     global x
#     x=10
# func()
# print(x)

# # closure
# def power(n):
#     def base(m):
#         return m**n
#     return base
# f=power(2)
# g=power(3)
# print(f(3))
# print(g(3))