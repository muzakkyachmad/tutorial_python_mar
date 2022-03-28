#trial from handnotes 15 pages

#19. functions
#function definitions sample 1
def area(b, h):
    """calculate area of rectangle"""
    A = b * h
    return A


def perimeter(b, h):
    """calculate perimieter of rectangle"""
    P = 2 * (b+h)
    return P

#main program using defined functions
width = 5
height = 3
print("Area = ", area(width, height))
print("Perimeter = ", perimeter(width, height))

#function definition sample 2
def area_and_perimeter(b, h):
    A = b * h
    P = 2 * (b + h)
    return A,P


ar, per = area_and_perimeter(4, 3)
print(f"the area is {ar} meter square")
print(per)



def main():
    print("Hello world!")

if __name__ == "__main__":
    main()

print("zakky")

print("value in built variable name is: ",__name__)



#20. avoiding for loops vector functions

import numpy as np

#calculate 100 values for x and y without a for loop
x = np.linspace(0, 2* np.pi, 100)
y = np.sin(x)

print(x)
print(y)


#21. diagrams
from numpy import linspace, sin, exp, pip
import matplotlib.pyplot as mp

#calculate 500 values for x and y without a for loop
x = linspace(0, 10*pi, 500)
y = sin(x) * exp(-x/10)

#to make diagram
mp.plot(x,y)
mp.show()








