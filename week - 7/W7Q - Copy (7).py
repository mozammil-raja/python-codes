inpt = list(map(int, input("Enter numbers : ").split()))
num = list(set(inpt))
if len(num) < 2:
    print("invalid input")
else:
    Lar = max(num[0], num[1])
    lar2 = min(num[0], num[1])
    for x in range(2, len(num)):
        if num[x] > Lar:
            lar2 = Lar
            Lar = num[x]
        elif num[x] > lar2:
            lar2 = num[x]
    print(f"Second largest element: {lar2}")


