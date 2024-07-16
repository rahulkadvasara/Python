import numpy as np
a = np.arange(12).reshape(3,4)
print(a)


# Using normal for loop iteration
for row in a:
    for cell in row:
        print(cell)

# For loop with flatten
for cell in a.flatten():
    print(cell)

# nditer
# C style ordering
for x in np.nditer(a, order='C'):
    print(x)
# Fortan style ordering
for x in np.nditer(a, order='F'):
    print(x)


# external_loop
for x in np.nditer(a, flags=['external_loop'],order='F'):
    print(x)

# Modify array values while iterating

for x in np.nditer(a, op_flags=['readwrite']):
    x[...] = x * x
print(a)

# Iterate two broadcastable arrays concurrently
b = np.arange(3, 15, 4).reshape(3,1)
print(b)

for x, y in np.nditer([a,b]):
    print (x,y)


