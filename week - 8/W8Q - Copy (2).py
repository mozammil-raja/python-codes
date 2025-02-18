list1 = list(map(int, input("Enter elements of first list: ").split()))
list2 = list(map(int, input("Enter elements of second list: ").split()))

mergedSet= set()

ls=list1+list2

for x in list1:
    mergedSet.add(x)

for x in list2:
    mergedSet.add(x)

print(f"union of set : {mergedSet}")
print(f"union of list : {ls}")

# 1 2 3 4 5
