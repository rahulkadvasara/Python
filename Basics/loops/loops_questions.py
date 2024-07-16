# # positive numbers
# num = [1,-2,3,-4,5,6,-7,-8,9,10]
# count = 0
# for n in num:
#     if n>=0:
#         count+=1
# print(count)

# # sum of even numbers
# n=int(input("Enter a Number :\n"))
# sum = 0
# for i in range(1,n+1):
#     if i%2 == 0:
#         sum+=i
# print(sum)

# # multiplication table
# n=int(input("Enter a Number :\n"))
# for i in range(1,11):
#     if i == 5:
#         continue
#     print(n,'x',i,'=',n*i)

# # reverse string
# string=input("Enter a string :\n")
# rev = ""
# for char in string:
#     rev = char+rev
# print(rev)

# # first non repeted character
# string=input("Enter a string :\n")
# for char in string:
#     if string.count(char) == 1:
#         print(char)
#         break

# # Factorial
# n=int(input("Enter a Number :\n"))
# fac = 1
# while n>0:
#     fac *= n
#     n-=1
# print("Factorial =",fac)

# # validate input b/w 1-10
# while True:
#     n=int(input("Enter a Number :\n"))
#     if 1<= n<=10:
#         print("Thanks")
#         break
#     else:
#         print("Invalid input,try again")

# # prime number
# n=int(input("Enter a Number :\n"))
# prime = True
# if n>1:
#     for i in range(2,n):
#         if(n%i==0):
#             prime = False
#             break
# if(prime):
#     print("It's a prime number")
# else:
#     print("It's not a prime number")

# # unique 
# items = ["apple","banana","orange","apple","mango"]
# unique = set()
# for item in items:
#     if item in unique:
#         print("Duplicate : ",item)
#         break
#     unique.add(item)

# # Exponential Backoff
# import time
# wait_time = 1
# max_retries = 5
# attempts = 0
# while attempts<max_retries:
#     print("Attemt",attempts+1,"-wait time",wait_time)
#     time.sleep(wait_time)
#     wait_time*=2
#     attempts+=1

