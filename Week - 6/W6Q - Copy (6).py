a, b, c = map(float, input("Enter three sides of the triangle: ").split())

if a + b > c and a + c > b and b + c > a:
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print("Area of the triangle:", area)

    if a == b == c:
        print("Triangle type: Equilateral")
    elif a == b or b == c or a == c:
        print("Triangle type: Isosceles")
    else:
        print("Triangle type: Scalene")
else:
    print("Invalid triangle sides")
