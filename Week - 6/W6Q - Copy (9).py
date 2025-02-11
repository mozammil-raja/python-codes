def isConsecutive(lst):
    return sorted(lst) == list(range(min(lst), max(lst) + 1))

lst = list(map(int, input("Enter n numbers : ").split()))

if isConsecutive(lst):
    print("The list contains consecutive integers.")
else:
    print("The list does not contain consecutive integers.")
