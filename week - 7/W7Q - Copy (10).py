def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
unique_numbers = list(set(numbers))  # Remove duplicates

if len(unique_numbers) < 2:
    print("No second largest number")
else:
    bubble_sort(unique_numbers)
    print("Second largest number is:", unique_numbers[-2])
