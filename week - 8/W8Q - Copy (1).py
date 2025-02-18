
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if len(arr[j]) > len(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

words = list(input("Enter words : ").split())
print(bubbleSort(words))


# my name is mozammil 445 778 78945 c a



