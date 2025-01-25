def gcd(n1, n2):
    if n2 == 0:
        return n1
    return gcd(n2, n1 % n2)

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

print("greatest common Factor of {num1} and {num2}:", gcd(num1, num2))