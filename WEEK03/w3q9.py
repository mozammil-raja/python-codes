a = int(input("Enter a: "))
b = int(input("Enter b: "))

print("Before:", a, b)

a = a + b
b = a - b
a = a - b

print("After:", a, b)