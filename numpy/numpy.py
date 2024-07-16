import numpy as np
import time
import sys

# comparing numpy and python list speed
size=100000

l1=range(size)
l2=range(size)

a1=np.arange(size)
a2=np.arange(size)

# python list
start=time.time()
result=[(x+y) for x,y in zip(l1,l2)]
print("Python took: ",((time.time()-start)*1000))

# numpy array
satrt=time.time()
result=a1+a2
print("numpy took: ",((time.time()-start)*1000))

# comparing numpy and python list memory usage

# python list
l=range(1000)
print(sys.getsizeof(5)*len(l))

# numpy array
array=np.arange(1000)
print(array.size*array.itemsize)