list1 = list(map(int, input("Enter elements of first list: ").split()))
list2 = list(map(int, input("Enter elements of second list: ").split()))

ls1= set(list1)
ls2= set(list2)

interSectionlist=list()
for x in ls1:
    if x in ls2:
        interSectionlist.append(x)

print(f"Intersection of {list1} and {list2} : {interSectionlist}")

# 1 2 3 4 5 6 7 8 9 12
# 10 11 12 13 14 15 1 2 3 4