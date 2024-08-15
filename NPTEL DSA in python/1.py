# question 1
# def h(x):
#     (d,n) = (1,0)
#     while d <= x:
#         (d,n) = (d*3,n+1)
#     return(n)
# print("h=",h(27993))


# question 2
# def g(n): 
#     s=0
#     for i in range(2,n):
#         if n%i == 0:
#            s = s+1
#     return(s)
# print(g(60)-g(48))

# q 3
# def f(n): 
#     s=0
#     for i in range(1,n+1):
#         if n//i == i and n%i == 0:
#            s = 1
#     return(s%2 == 1)
# print(f(16))

# q 4
def foo(m):
    if m == 0:
      return(0)
    else:
      return(m+foo(m-1))
print(foo(10))