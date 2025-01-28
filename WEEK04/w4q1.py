

# Average
def AvgValue(num, l):
    x= num/l
    return x

# Conversion
def CalCulateFaren(cel):
    f=((9/5)*cel + 32)
    return f

# Perimetre
def CalculatePerimeter(l, b):
    peri=2*(b+l)
    return peri


# Average
arr = [0] * 5
print(arr)
sum= 0
for i in range(0, 5):
    arr[i]=int(input(f"{i}. Enter Number : "))
    sum+=arr[i]
print(f"Average : {AvgValue(sum, 5)}")

# Conversion
celcius = float(input("Enter Temprature (Celsius): "))
print(f"{celcius}C is equal to {CalCulateFaren(celcius)}F")

# Perimetre
Length=(int)(input("Enter length : "))
Breadth=(int)(input("Enter breadth : "))
print(f"perimeter of rectangle with Length: {Length} and Breadth: {Breadth} = {CalculatePerimeter(Length, Breadth)}")
