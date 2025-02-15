def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

list1 = list(map(int, input("Enter elements [ 1st list ]: ").split()))
list2 = list(map(int, input("Enter elements [ 2nd list ]: ").split()))

MergedList=bubbleSort(list1+list2)
print(f"{MergedList}")