# Write circle_calc() function that takes radius of a circle as an input from user and then 
# it calculates and returns area, circumference and diameter. You should get these values in your main program 
# by calling circle_calc function and then print them

import math

def circle_calc(r):
    area = math.pi*(r**2)
    circumference = 2*math.pi*r
    diameter = 2*r
    return area,circumference,diameter

def main():
    r = float(input("Enter the radius of circle: "))
    a,c,d = circle_calc(r)
    print(f"Area : {round(a,2)}\nCircumference : {round(c,2)}\nDiameter : {round(d,2)}")

if __name__ == '__main__':
    main()