lst = [1, 'a', 2, 'b', 3, 4, 'c']

sumNumbers = 0

for i in lst:
    if isinstance(i, (int, float)):
        sumNumbers += i

print("Sum of numbers:", sumNumbers)
