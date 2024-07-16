import numpy as np
a=np.array([[1,2],[3,4],[5,6]])
print(a.ndim)  # --> dimension of an array
print(a.itemsize)  # --> size of an element
print("datatype of a is : ",a.dtype)

x=np.array([[1,2],[3,4]],dtype=np.float64)
print("datatype of x is : ",x.dtype)

print("size of a is : ",a.size)
print("shape of a is : ",a.shape)

print(np.zeros(3,4))  # --> initializes array with zeros

print(np.arange(1,5))
print(np.arange(1,5,2))

print(np.linspace(1,5,10))

print(a.reshape(2,3))

print(a.ravel())  # -->returns a flatern array
      
print(a.min())
print(a.max())
print(a.sum())
print(a.sum(axis=0))
print(a.sum(axis=1))

np.sqrt(a)
np.std(a)   # --> standerd daviation

b=np.array([[8,9],[3,1],[5,2]])

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a.dot(b))

print(a[1,2])
print(a[0:2,2])
print(a[-1])

print(a.flatten())

print(np.vstack((a,b)))
print(np.hstack((a,b)))

p=np.array([1,2,3,4,5,6,7,8,9],[9,8,7,6,5,4,3,2,1])

print(np.hsplit(p,3))
print(np.vsplit(p,2))

z=np.arange(12).reshape(3,4)

y=z>4
print(y)
print(z[y])

z[y]=-1
print(z[y])

