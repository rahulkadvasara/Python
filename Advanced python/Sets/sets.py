basket={'apple','mango','orange','mango','orange'}
print(type(basket))
print(basket)

a=set()
a.add(1)
a.add(2)
print(a)

x={'a','b','c'}
y={'a','g','h'}

print('a' in x)
print('g' in x)

for i in x:
    print(i)

print(x|y)
print(x&y)
print(x-y)

print(x<y)

x={'g','h'}

print(x<y)
