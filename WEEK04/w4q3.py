from math import pi

def AreaCircle (rad):
    return pi * rad ** 2

radius = float(input("Enter radius: "))
if radius>=1 :
    print(f"Area of circle {AreaCircle(radius)}")
else:
    print("Enter A positive Integer")