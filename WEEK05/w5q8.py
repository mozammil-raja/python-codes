str_input = input("Enter a string: ")
charArray = list(str_input)
n = len(charArray)
s=""

for i in range(n-1, -1, -1):
    s+=charArray[i]+" "

print(s)