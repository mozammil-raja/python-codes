number = list(map(int, input("Enter numbers : ").split()))
evenList = [num for num in number if num % 2 == 0]
oddList = [num for num in number if num % 2 != 0]

print("Even numbers:", evenList)
print("Odd numbers:", oddList)


# Every list comprehension in Python includes three elements:

# expression is the member itself, a call to a method, or any other valid expression that returns a value. 
#             In the example above, the expression number * number is the square of the member value.

# member is the object or value in the list or iterable. In the example above, the member value is number.

# iterable is a list, set, sequence, generator, or any other object that can return its elements one at a time.
#         In the example above, the iterable is range(10).