from math import pi

radius = float(input("Enter Radius Of Sphere: "))
volume = (4/3) * pi * (radius ** 3)
if radius>=1 :
    print(f"Volume of Sphere whose radius is {radius}: {volume}")
else:
    print("Enter A positive Integer")
