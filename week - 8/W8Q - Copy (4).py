n = int(input("Enter the number of elements: "))
numbers = [i for i in range(1, n + 1)]

result = [(num, num ** 2) for num in numbers]
print("List of tuples:", result)
