a, b, c = map(int, input("Enter three numbers: ").split())

if a > b and a > c:
    print("Greatest number is:", a)
if b > c:
    print("Greatest number is:", b)
if c > b:
    print("Greatest number is:", c)
