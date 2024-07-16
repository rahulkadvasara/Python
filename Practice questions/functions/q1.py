# # area of a triangle
# base = int(input("Enter the base of triangle : "))
# height = int(input("Enter the height of triangle : "))
# def area(base,height):
#     return (1/2)*base*height
# print(area(base,height))

# area based on shape
def area(d1,d2,shape = "triangle"):
    if shape == "rectangle":
        return d1*d2
    else:
        return (1/2)*d1*d2

shape = input("Enter the shape : ")
d2 = int(input("Enter the first diamension : "))
d1 = int(input("Enter the second diamension : "))

print(area(d1,d2,shape))