def isConsecutive(ls):
    r = 0
    while r < len(ls):
        i = r
        while i + 1 < len(ls) and ls[i + 1] - ls[i] == 1:
            i += 1
        if i > r:
            for j in range(r, i + 1):
                print(ls[j], end=", " if j < i else "\n")
        r = i + 1

lst = list(map(int, input("Enter numbers: ").split()))
lst.sort()
print(f"Sorted list: {lst}")
isConsecutive(lst)
# 1 2 3 4 65 76 65 15 16 17
#1 2 3 56 67 8 9 10