list1 = list(map(int, input("Enter elements of first list: ").split()))
list2 = list(map(int, input("Enter elements of second list: ").split()))

merged_list = sorted(list1 + list2)
print("Merged and sorted list:", merged_list)
