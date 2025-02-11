list1 = list(map(int, input("Enter elements of first list: ").split()))
list2 = list(map(int, input("Enter elements of second list: ").split()))

intersection_list = list(set(list1) & set(list2))
print("Intersection of lists:", intersection_list)
