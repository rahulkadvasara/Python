# # squatre function
# n=int(input("Enter a number:\n"))
# def square(n):
#     return n**2
# result = square(n)
# print(result)

# # multiple perameter
# a=int(input("Enter first number:\n"))
# b=int(input("Enter second number:\n"))
# def sum(a,b):
#     return a+b
# result = sum(a,b)
# print(result)

# # multiply function
# def multiply(a,b):
#     return a*b
# print(multiply(4,6))
# print(multiply(4,'a'))

# # returns multiple values
# import math
# r = int(input("Enter a number:\n"))
# def circle(r):
#     area = math.pi*(r**2)
#     circumference = 2*math.pi*r
#     return area,circumference
# a,c=circle(r)
# print("Area: ",a,"\nCircumference: ",c)

# # greet
# def greet(name="User"):
#     return "Hello "+name+" !"
# print(greet("Rahul"))
# print(greet())

# # lambda function
# n=int(input("Enter a number:\n"))
# cube = lambda n:n**3
# print(cube(2))

# # *args function of sum
# def sum_all(*args):
#     print(*args)
#     print(args)
#     for i in args:
#         print(i*2)
#     return sum(args)
# print(sum_all(1,2,3))
# # print(sum_all(1,2,3,4,5))

# # Function with **kwargs
# def print_kwargs(**kwargs):
#     for key,value in kwargs.items():
#         print(f'{key} : {value}')
# print_kwargs(name = "xyz",power = "lazer",enemy="abc")

# # yield
# limit = int(input("Enter a Number:\n"))
# def even_generator(limit):
#     for i in range(2,limit+1,2):
#         yield i
# for num in even_generator(limit):
#     print(num)

# # recursive function to calculate factorial
# n = int(input("Enter a Number:\n"))
# def fac(n):
#     if n == 0 or n == 1 :
#         return 1
#     else:
#         return n*fac(n-1)
# print(fac(n))

