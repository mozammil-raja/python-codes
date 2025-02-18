numbers =list(map(int, input("Enter Element : ").split()))
print(f"Entered List : {numbers}")

result = [(num, num ** 2) for num in numbers]
print("List of tuples:", result)
