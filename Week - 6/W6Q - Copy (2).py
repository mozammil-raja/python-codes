a, b, c = map(int, input("Enter three numbers: ").split())

if a < b and a < c:
    print("Smallest number is:", a)
else:
    if b < c:
        print("Smallest number is:", b)
    else:
        print("Smallest number is:", c)
