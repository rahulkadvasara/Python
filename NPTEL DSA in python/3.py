# programming assignment 1
# def contracting(l):
#   if len(l)<3:
#     return True
#   return((abs(l[1]-l[0])>abs(l[2]-l[1])) and contracting(l[1:]))

# def counthv(l):
#   hills=0
#   valleys=0
#   for i in range(1,len(l)-1):
#     if l[i-1]<l[i]>l[i+1]:
#       hills+=1
#     if l[i-1]>l[i]<l[i+1]:
#       valleys+=1
#   return([hills,valleys])

# def leftrotate(m):
#   size=len(m)
#   rotate_m=[]
#   for i in range(size):
#     rotate_m.append([])
#   for c in range(size-1,-1,-1):
#     for r in range(size):
#       rotate_m[size-(c+1)].append(m[r][c])
#   return rotate_m

