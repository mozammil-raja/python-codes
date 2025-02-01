from math import pi
import math

def GreatestNum(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print(f"{num1} is greatest")
    elif num2 > num1 and num2 > num3:
        print(f"{num2} is greatest")
    else:
        print(f"{num3} is greatest")

#Cylinder
def VolumeOfCyl(r, h):
    z= pi * (r ** 2) * h
    print(f"Volume of Cylinder: {z}")

#cube
def VolumeOfCube(l):
     print(f"Volume of Cube : {l**3}")

#Rect Box
def VolumeOfRectBox(l, b, h):
    print(f"Volume of Rect Box : {l * b * h}")

# area of rectangle
def AreaRect(l , b):
    print(f"Area of Rectangle : {l * b }")

# circumference
def CircumferenceOfCircle(r):
    print(f"Circumference of Circle : {2 * pi * r}")

#Swapped
def SwapX(a, b):
    z=a
    a=b
    b=z
    print("After Swap")
    print(f"a={a}, b={b}")


x=1
while(x):
    print("CHOOSE Option (Press NUM Button) : ")
    print("1. Find Greatest Number : ")
    print("2. Calculate volume : ")
    print("3. Calculate Area : ")
    print("4. Swap Two Variable ")
    print("5. Calculate Distance : ")
    print("0. Exit")
    
    opt=int(input("Enter Option :- "))
    match opt:
            case 1:
                print("1. Greatest Number Section: ")
                num1, num2, num3=map(int, input("Enter Option :- ").split())
                GreatestNum(num1, num2,num3)
            case 2:
                print("2. volume Section: ")
                t=1
                while(t):
                    print("CHOOSE Option")
                    print("1. Cylinder : ")
                    print("2. Cube : ")
                    print("3. Rectangle Box")
                    print("0. CHANGE OPTION")
                    optx=int(input("Enter Option :- "))
                    match optx:
                        case 1:
                            print("1. Cylinder")
                            radius, height=map(int, input("Enter radius and height of Cylinder :- ").split())
                            VolumeOfCyl(radius, height)
                        case 2:
                            print("1. Cube")
                            lent = int(input("Enter Length of Cube :- "))  
                            VolumeOfCube(lent)
                        case 3:
                            print("1. Rectangle Box")
                            length, breadth, height = map(int, input("Enter length, breadth, height :- ").split())
                            VolumeOfRectBox(length, breadth, height)
                        case 0:
                            t = 0 
                        case default:
                            print("Invalid key")
            case 3:
                print("3. Area Section: ")
                p=1
                while(p):
                    print("CHOOSE Option")
                    print("1. Area of Rectangle : ")
                    print("2. Circumference of Circle : ")
                    print("0. CHANGE OPTION")
                    optx=int(input("Enter Option :- "))
                    match optx:
                        case 1:
                            print("1. Area of Rectangle : ")
                            length, breadth = map(int, input("Enter length, breadth :- ").split())
                            AreaRect(length, breadth)
                        case 2:
                            print("2. Circumference of Circle : ")
                            rad = int(input("Enter radius :- "))  # Directly unpack the value
                            CircumferenceOfCircle(rad)
                        case 0:
                            p = 0 
                        case default:
                            print("Invalid key")
            case 4:
                print("4. Swap Section: ")
                num11, num12 = map(int, input("Enter Two :- ").split())
                print("Before Swap")
                print(f"a={num11}, b={num12}")
                SwapX(num11, num12)
            case 5:
                print("5. Distance section: ")
                num111, num222 = map(int, input("Enter X1 and Y1 :- ").split())
                num121, num232 = map(int, input("Enter X2 and Y2 :- ").split())
                p = [num111, num222]
                q = [num121, num232]
                print(f"Total Distance between point X1={num111}, Y1={num222} to X2={num121}, Y2={num232} is {math.dist(p, q)}")

            case 0:
                x = 0
            case default:
                print("Invalid input ")
