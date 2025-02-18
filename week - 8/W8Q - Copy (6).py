
string = input("Enter a string: ")

count={}

for x in string:
    if x in count:
        count[x]+=1
    else:
        count[x]=1

print(count)