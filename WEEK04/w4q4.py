def Factcorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact

number = int(input("Enter a Number: "))

if number>=1 :
    print(f"Factorial of {number} is {Factcorial(number)}")
else:
    print("Enter A positive Integer")

