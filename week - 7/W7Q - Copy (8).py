numbers = list(map(int, input("Enter numbers separated by space: ").split()))
even_list = [num for num in numbers if num % 2 == 0]
odd_list = [num for num in numbers if num % 2 != 0]

print("Even numbers:", even_list)
print("Odd numbers:", odd_list)
