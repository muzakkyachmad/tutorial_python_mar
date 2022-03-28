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



#avoiding for loops vector functions

import numpy





