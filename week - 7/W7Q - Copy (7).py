numbers = list(map(int, input("Enter numbers separated by space: ").split()))
unique_numbers = list(set(numbers))  # Remove duplicates

if len(unique_numbers) < 2:
    print("No second largest number")
else:
    unique_numbers.sort(reverse=True)
    print("Second largest number is:", unique_numbers[1])
