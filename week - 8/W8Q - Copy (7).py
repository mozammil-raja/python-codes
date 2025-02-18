
word = list(map(str, input("Enter a String: ").split()))
SortedList=list()

for x in word:
    ls=list(x)
    ls.sort()
    SortedList.append("".join(ls))

print(SortedList)

for x in SortedList:
    print(x[::-1],end=" ")


