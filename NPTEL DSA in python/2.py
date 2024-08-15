# q1
# x = [[3,5],"mimsy",2,"borogove",1]  # Statement 1
# y = x[0:50]                          # Statement 2
# z = y                                # Statement 3
# w = x                                # Statement 4
# x[1] = x[1][:5] + 'ery'              # Statement 5
# y[1] = 4                             # Statement 6
# w[1][:3] = 'fea'                     # Statement 7
# z[4] = 42                            # Statement 8
# x[0][0] = 5555                       # Statement 9
# a = (x[3][1] == 1)                   # Statement 10

# q2
# b = [43,99,65,105,4]
# a = b[2:]
# d = b[1:]
# c = b
# d[1] = 95
# b[2] = 47
# c[3] = 73

# q3
# startmsg = "anaconda"
# endmsg = ""
# for i in range(1,1+len(startmsg)):
#   endmsg = endmsg + startmsg[-i]
# print(endmsg)


# q4
# def mystery(l):
#   l = l[2:]
#   return(l)
# mylist = [7,11,13,17,19,21]
# print(mystery(mylist))



# programming assignment 1
# def intreverse(n):
#     r=0
#     while ( n != 0 ):
#         r = (r*10)+(n % 10)
#         n = n // 10
#     return(r)  
  
# def matched(s):
#   sum = 0
#   for i in range(len(s)):
#     if (s[i] == '('):
#       sum+=1
#     elif(s[i]==')'):
#       sum-=1
#     if(sum<0):
#       break
#   if(sum==0):
#     return True
#   else:
#     return False     
          
# def factors(n):
#   factorlist=[]
#   for i in range(1,n+1):
#     if n%i==0:
#       factorlist.append(i)
#   return(factorlist)

# def isprime(n):
#   return(factors(n)==[1,n])

# def sumprimes(l):
#   sum=0
#   for i in range(len(l)):
#       if(isprime(l[i])):
#         sum+=l[i]
#   return (sum)
