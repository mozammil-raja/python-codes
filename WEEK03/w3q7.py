num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number: "))

print("Before: ", num1, num2)

num1 = num1 ^ num2
num2 = num1 ^ num2
num1 = num2 ^ num1

print("After: ", num1, num2)