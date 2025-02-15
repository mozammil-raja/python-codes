def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

numbers = list(map(int, input("Enter number: ").split()))

if len(numbers) < 2:
    print("must contain at least 2 num")
else:
    sortedNumber = bubbleSort(numbers)
    print("Sorted List:", sortedNumber)
    print("Second largest :", sortedNumber[-2])

# 4 5 2 78 9 2 56 45 33 33 33 0 1