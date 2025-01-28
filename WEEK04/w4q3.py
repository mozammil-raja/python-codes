from math import pi

def c_area (rad):
    return pi * rad ** 2

rad = float(input("Enter radius: "))
print(f"Area of circle {c_area(rad)}")