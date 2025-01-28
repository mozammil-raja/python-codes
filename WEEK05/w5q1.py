from math import pi

# largest of three nums
def find_largest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

# volume of cylinder
def vol_cyl(r, h):
     return pi * (r ** 2) * h

# volume of cube
def vol_cube(a):
    return a ** 3

# volume of cuboid
def vol_rect_box(l, b, h):
    return l * b * h

# area of rectangle
def area_rect(l , b):
    return l * b

# circumference
def circum(r):
    return 2 * pi * r

# swap two variables
def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b

