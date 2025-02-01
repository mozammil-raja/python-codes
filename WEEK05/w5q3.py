s = input("Enter a string: ")
charArray = list(s)
n=len(charArray)
str=""
for i in range(1, n, 2):
    str+=charArray[i]

print(str)

