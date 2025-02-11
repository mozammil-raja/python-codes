list1 = list(map(int, input("Enter elements of first list: ").split()))
list2 = list(map(int, input("Enter elements of second list: ").split()))

union_list = list(set(list1) | set(list2))
print("Union of lists:", union_list)
